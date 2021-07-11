import pandas as pd

#Handige functies
def correction(parameter, lower, upper):
    "calculates and returns corrected parameter based on lower/upper bounds"
    corrected = abs((lower - parameter)) / abs(lower - upper)
    return corrected

def get_data(filename):
    "retrieves data to create necessary dataframe(s)"
    return pd.read_excel(filename, index_col=0)
