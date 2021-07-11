#Imports
import pandas as pd
import requests
from datetime import date
import numpy as np
from backend.utils import correction, get_data

class DA40():
    def __init__(self, press_alt=4000, temperature=22, fuel=15, bagage=10,
                 pax_amount=3, wind=10, airport_dep='EHRD', airport_arr='EHEH',
                 date_flight='2021-07-05'):
        """The Diamond DA40 Diamond Star class.

        Initializes all features needed to ultimately calculate
        take off distance based on the given parameters.

        Parameters
        -----------
        press_alt: int
            Pressure Altitude in feet, default = 1000
        temperature: int
            Temperature in degrees Celcius, default = 18
        fuel: int
            Fuel in USgal, default = 20
        bagage: int
            Bagage in kg, default = 10
        pax_amount: int
            Number of passengers, default = 2
        wind: int
            Wind component, default = 5
        airport_dep: string
            Airport of departure, default = 'EHRD'
        airport_arr: string
            Airport of arrival, default = 'EHEH'
        date_flight: string
            Date of flight, default = '2021-07-05'
        
        Returns
        ----------
        None
        """
        self.press_alt = press_alt
        self.temperature = temperature
        self.fuel = fuel
        self.bagage = bagage
        self.pax_amount = pax_amount
        self.wind = wind
        self.airport_dep = airport_dep
        self.airport_arr = airport_arr
        self.date_flight = date_flight
        self.pax1, self.pax2, self.pax3, self.pax4 = (75, 83, 60, 0)
        self.OVERWEIGHT, self.MOMENTRANGE, self.TAKEOFFDIST, self.TAILWIND = (False, False, False, False)
        self.weight, self.moment, self.step1, self.step2, self.takeoff_distance = (0, 0, 0, 0, 0)
        self.log = []
    
    def get_compute_parameters(self):
        "return relevant compute parameters and takeoff distance for instance"
        return (self.weight, self.moment, self.step1, 
                self.step2, self.takeoff_distance)
    def get_metar_parameters(self):
        "retrieve relevant metar parameters for given flight date"
        self.METAR_arr = requests.get('https://api.met.no/weatherapi/tafmetar/1.0/metar?date='+ self.date_flight + '&icao=' + self.airport_arr)
        self.METAR_dep = requests.get('https://api.met.no/weatherapi/tafmetar/1.0/metar?date='+ self.date_flight + '&icao='+ self.airport_dep)
        self.TAF_arr = requests.get('https://api.met.no/weatherapi/tafmetar/1.0/taf?date=' + self.date_flight + '&icao=' + self.airport_arr)
        self.TAF_dep = requests.get('https://api.met.no/weatherapi/tafmetar/1.0/taf?date=' + self.date_flight + '&icao=' + self.airport_dep)
    
    def calculate_step1(self, filename, frameweight=797):
        da40_pressalt = get_data(filename)
        press_list = pd.Index.tolist(da40_pressalt.index)
        for (index, press) in enumerate(press_list):
            if press < self.press_alt:
                continue
            else: 
                upper = da40_pressalt.loc[press,self.temperature]
                lower = da40_pressalt.loc[press_list[index-1],self.temperature]
                press_cor = correction(self.press_alt, press_list[index-1], press_list[index])
                break

        delta_step1 = (upper - lower) * press_cor
        frameweight = 797
        front_seats = self.pax1 + self.pax2
        rear_seats = self.pax3 + self.pax4
        self.weight = frameweight + self.pax1 + self.pax2 + self.pax3 + self.pax4 + self.fuel*3.07 + self.bagage
        weight_moment = frameweight*2.43 + front_seats*2.30 + rear_seats*3.25 + self.fuel*2.63*3.07 + self.bagage*3.65
        self.moment = weight_moment / self.weight
        self.step1 = delta_step1 + lower
        self.log.append(f"Step 1: {self.step1}")
    
    def safety_checks(self):
        self.TAILWIND = self.wind < -10
        self.OVERWEIGHT = self.weight > 1150
        self.MOMENTRANGE = ((self.weight < 980 and self.moment < 2.40) 
                            or (self.moment > 2.59))
        if self.weight > 980 and self.moment < 2.46 or self.moment > 2.59:
            maxweight = 2833.333333333333 * (self.moment-2.40) + 980
            if self.weight >= maxweight:
                self.MOMENTRANGE = True
        if self.press_alt == int(10000) and self.temperature > int(26):
            self.TAKEOFFDIST = True
        elif self.press_alt == int(9500) and self.temperature > int(29):
            self.TAKEOFFDIST = True
        elif self.press_alt == int(9000) and self.temperature > int(34):
            self.TAKEOFFDIST = True
        elif self.press_alt == int(8500) and self.temperature > int(36):
            self.TAKEOFFDIST = True
        elif self.press_alt == int(8000) and self.temperature > int(42):
            self.TAKEOFFDIST = True
        elif self.press_alt == int(7500) and self.temperature > int(45):
            self.TAKEOFFDIST = True
    
    def calculate_step2(self, filename):
        UNSAFE = (self.OVERWEIGHT or self.MOMENTRANGE or self.TAKEOFFDIST)
        self.log.append(f"UNSAFE should be False: {UNSAFE}")
        if not UNSAFE:
            da40_weight = pd.read_excel(filename, index_col=0, sheet_name=1)
            distance_list = pd.Index.tolist(da40_weight.index)
            kg_list = pd.Index.tolist(da40_weight.columns)
            for (index, dist1) in enumerate(distance_list):
                if dist1 < self.step1:
                    continue
                else:
                    lower = distance_list[index-1]
                    upper = distance_list[index]
                    dist_corr = correction(self.step1, lower, upper)
                    lower_dist = np.array(da40_weight.loc[lower, :])
                    upper_dist = np.array(da40_weight.loc[upper, :])
                    break
            delta_dist_array = upper_dist - lower_dist
            corrected_dist_array = np.array((delta_dist_array * dist_corr) + lower_dist)
            for (index, kilo) in enumerate(kg_list):
                if kilo > self.weight:
                    continue
                else:
                    upperbound = corrected_dist_array[index-1]
                    lowerbound = corrected_dist_array[index]
                    upperkg = kg_list[index-1]
                    lowerkg = kg_list[index]
                    kg_corr = correction(self.weight, lowerkg, upperkg)
                    break
            delta = abs(upperbound - lowerbound)
            self.step2 = (delta * kg_corr) + lowerbound
            self.log.append(f"Step 2: {self.step2}")

    def calculate_takeoff_distance(self, filename):
        da40_wind = pd.read_excel(filename, index_col=0, sheet_name=2)
        distance_list = pd.Index.tolist(da40_wind.index)
        wind_list = da40_wind[self.wind].values.tolist()
        if not self.TAILWIND:
            for (index, dist) in enumerate(distance_list):
                if dist < self.step2:
                    continue
                else:
                    lower = distance_list[index-1]
                    upper = distance_list[index]
                    wind_corr = correction(self.step2, lower, upper)
                    lowerwind = wind_list[index-1]
                    upperwind = wind_list[index]
                    delta = abs(upperwind - lowerwind)
                    self.takeoff_distance = (delta * wind_corr) + lowerwind
                break

    def pipeline(self, filename):
        self.calculate_step1(filename)
        self.safety_checks()
        self.calculate_step2(filename)
        self.calculate_takeoff_distance(filename)
        return self.takeoff_distance