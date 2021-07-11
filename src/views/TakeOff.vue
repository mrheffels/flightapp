<template>
  <v-container fluid>
    <v-form
      ref="form"
      v-model="valid"
      lazy-validation
    >
      <!-- <v-file-input
      accept=".xls,.xlsx"
      label="Airframe data input"
      ></v-file-input> -->
      <v-autocomplete
        v-model="airport"
        :items="airports"
        :rules="[v => !!v || 'Item is required']"
        auto-select-first
        clearable
        required
        prepend-icon="mdi-airplane-takeoff"
        label="Airport of Departure"
        placeholder="Start typing to Search"
      ></v-autocomplete>
      <v-text-field
        v-model="pressAlt"
        :counter="5"
        :rules="pressAltRules"
        label="Pressure Altitude"
        required
      ></v-text-field>
      <v-text-field
        v-model="temperature"
        :counter="2"
        :rules="tempRules"
        label="Temperature in degrees Celcius"
        required
      ></v-text-field>
      <v-text-field
        v-model="bagage"
        :counter="3"
        :rules="bagageRules"
        label="Bagage in Kg"
        required
      ></v-text-field>
      <v-row>
        <v-col cols="2">
          <v-switch
            color="primary"
            value
            input-value="true"
            disabled
          ></v-switch>
        </v-col>
        <v-col cols="10">
          <v-text-field
          v-model="weightPilot"
          :counter="3"
          :rules="weightRules"
          label="Weight Pilot"
          required
        ></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="2">
          <v-switch
            v-model="pax1"
            color="primary"
          ></v-switch>
        </v-col>
        <v-col cols="10">
          <v-text-field
          v-model="weightPassenger1"
          :counter="3"
          :rules="weightRules"
          label="Weight Passenger 1"
          :disabled="!pax1"
        ></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="2">
          <v-switch
            v-model="pax2"
            color="primary"
          ></v-switch>
        </v-col>
        <v-col cols="10">
          <v-text-field
          v-model="weightPassenger2"
          :counter="3"
          :rules="weightRules"
          label="Weight Passenger 2"
          :disabled="!pax2"
        ></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="2">
          <v-switch
            v-model="pax3"
            color="primary"
          ></v-switch>
        </v-col>
        <v-col cols="10">
          <v-text-field
          v-model="weightPassenger3"
          :counter="3"
          :rules="weightRules"
          label="Weight Passenger 3"
          :disabled="!pax3"
        ></v-text-field>
        </v-col>
      </v-row>
      <v-text-field
        v-model="windComponent"
        :counter="2"
        :rules="windRules"
        label="Wind component"
        required
      ></v-text-field>
      <v-text-field
        v-model="fuel"
        :counter="2"
        :rules="fuelRules"
        label="Fuel in USgal"
        required
      ></v-text-field>
        <v-btn
          :disabled="!valid"
          color="primary"
          @click="calcStep1"
        >
          Next step
        </v-btn>
    </v-form>
  </v-container>
</template>

<script>

  export default {
    name: 'TakeOff',
    data: () => ({
      valid: false,
      airport: '',
      pressAlt: '0',
      temperature: '0',
      fuel: '15',
      bagage: '10',
      pax1: false,
      pax2: false,
      pax3: false,
      weightPilot: '70',
      weightPassenger1: '70',
      weightPassenger2: '70',
      weightPassenger3: '70',
      windComponent: '0',
      pressAltRules: [
        v => !!v || 'Pressure Altitude is required',
        v => (v || '').length <= 5 || 'Pressure Altitude has max 5 digits',
        v => (v && /^\d+$/.test(v)) || 'Pressure Altitude can only contain positive numbers',
      ],
      fuelRules: [
        v => !!v || 'Fuel is required',
        v => v !== '0' || 'Fuel cannot be zero',
        v => (v || '').length <= 2 || 'Fuel has max 2 digits',
        v => (v && /^\d+$/.test(v)) || 'Fuel can only contain positive numbers',
      ],
      bagageRules: [
        v => !!v || 'Bagage is required',
        v => (v || '').length <= 3 || 'Bagage has max 3 digits',
        v => (v && /^\d+$/.test(v)) || 'Bagage can only contain positive numbers',
      ],
      paxRules: [
        v => !!v || 'Pax Amount is required',
        v => v !== '0' || 'Pax Amount cannot be zero',
        v => (v || '').length <= 1 || 'Pax Amount has max 1 digit',
        v => (v && /^\d+$/.test(v)) || 'Pax Amount can only contain positive numbers',
      ],
      weightRules: [
        v => !!v || 'Weight is required',
        v => v !== '0' || 'Weight cannot be zero',
        v => (v || '').length <= 3 || 'Weight has max 3 digit',
        v => (v && /^\d+$/.test(v)) || 'Weight can only contain positive numbers',
      ],
      windRules: [
        v => !!v || 'Wind component is required',
        v => (v || '').length <= 2 || 'Wind component has max 2 digits',
        v => (v && /^-?\d+$/.test(v)) || 'Wind component can only contain real numbers',
      ],
      tempRules: [
        v => !!v || 'Temperature is required',
        v => (v || '').length <= 2 || 'Temperature has max 2 digits',
        v => (v && /^-?\d+$/.test(v)) || 'Temperature can only contain real numbers',
      ],
      airports: ['Tirana Airport - LATI', 'Yerevan Zvartnots Airport - UDYZ', 'Bakoe Airport - UBBB', 'Antwerp Airport - EBAW',
      'Brussels Airport - EBBR', 'Charleroi Airport - EBCI', 'Luik Airport - EBLG', 'Oostende Brugge Airport - EBOS', 'Sarajevo Airport - LQSA',
      'Tuzla Airport - LQTZ', 'Burgas Airport - LBBG', 'Sofia Airport - LBSF', 'Varna Airport - LBWN', 'Larnaca Airport - LCLK', 'Paphos Airport - LCPH',
      'Aalborg Airport - EKYT', 'Aarhus Airport - EKAH', 'Billund Airport - EKBI', 'Kopenhagen Airport - EKCH', 'Vágar Airport - EKVG', 'Allgäu Airport Memmingen - EDJA', 'Berlijn Brandenburg Airport - EDDB',
      'Bremen Airport - EDDW', 'Dortmund Airport - EDLW', 'Dresden Airport - EDDC', 'Düsseldorf Airport - EDDL', 'Frankfurt Airport - EDDF', 'Frankfurt-Hahn Airport - EDFH', 'Friedrichshafen Airport - EDNY',
      'Hamburg Airport - EDDH', 'Hannover Airport - EDDV', 'Karlsruhe Baden-Baden Airport - EDSB', 'Keulen Bonn Airport - EDDK', 'Leipzig Halle Airport - EDDP', 'München Airport - EDDM',
      'Münster Osnabrück Airport - EDDG', 'Nürnberg Airport - EDDN', 'Paderborn Lippstadt Airport - EDLP', 'Stuttgart Airport - EDDS', 'Weeze Airport - EDLV', 'Tallinn Airport - EETN',
      'Helsinki Airport - EFHK', 'Oulu Airport - EFOU', 'Rovaniemi Airport - EFRO', 'Tampere Airport - EFTP', 'Turku Airport - EFTU', 'Vaasa Airport - EFVA', 'Ajaccio Airport - LFKJ',
      'Bastia Airport - LFKB', 'Bergerac Airport - LFBE', 'Biarritz Airport - LFBZ', 'Bordeaux Airport - LFBD', 'Brest Bretagne Airport - LFRB', 'Figari South Corsica Airport - LFKF',
      'Lille Airport - LFQQ', 'Lyon-Saint Exupéry Airport - LFLL', 'Marseille Airport - LFML', 'Montpellier Airport - LFMT', 'Nantes Airport - LFRS', 'Nice Airport - LFMN',
      'Parijs Beauvais Airport - LFOB', 'Parijs Charles de Gaulle Airport - LFPG', 'Parijs Orly Airport - LFPO', 'Rennes Bretagne Airport - LFRN', 'Réunion Roland Garros Airport - FMEE',
      'Straatsburg Airport - LFST', 'Toulon-Hyères Airport - LFTH', 'Toulouse Blagnac Airport - LFBO', 'Kutaisi Airport - UGKO', 'Tbilisi Airport - UGTB', 'Athene Airport - LGAV', 'Chania Airport - LGSA',
      'Corfu Airport - LGKR', 'Heraklion Airport - LGIR', 'Kos Airport - LGKO', 'Mykonos Airport - LGMK', 'Rhodos Airport - LGRP', 'Santorini Airport - LGSR', 'Thessaloniki Airport - LGTS', 'Zakynthos Airport - LGZA',
      'Boedapest Airport - LHBP', 'Debrecen Airport - LHDC', 'Cork Airport - EICK', 'Dublin Airport - EIDW', 'Ireland West Airport Knock - EIKN', 'Kerry Airport - EIKY', 'Shannon Airport - EINN', 'Keflavik Airport - BIKF',
      'Alghero Airport - LIEA', 'Ancona Airport - LIPY', 'Bari Airport - LIBD', 'Bergamo Airport - LIME', 'Bologna Airport - LIPE', 'Brindisi Airport - LIBR', 'Cagliari Airport - LIEE', 'Catania Fontanarossa Airport - LICC',
      'Comiso Airport - LICB', 'Florence Airport - LIRQ', 'Genua Airport - LIMJ', 'Lamezia Terme Airport - LICA', 'Milaan Linate Airport - LIML', 'Milaan Malpensa Airport - LIMC', 'Napels Airport - LIRN', 'Olbia Costa Smeralda Airport - LIEO',
      'Palermo Airport - LICJ', 'Perugia Airport - LIRZ', 'Pescara Airport - LIBP', 'Pisa Airport - LIRP', 'Rome Ciampino Airport - LIRA', 'Rome Fiumicino Airport - LIRF', 'Trapani Airport - LICT', 'Treviso Airport - LIPH', 'Triëst Airport - LIPQ',
      'Turijn Airport - LIMF', 'Venetië Airport - LIPZ', 'Verona Airport - LIPX', 'Almaty Airport - UAAA', 'Nursultan Nazarbayev Airport - UACC', 'Pristina Airport - BKPR', 'Dubrovnik Airport - LDDU', 'Pula Airport - LDPL', 'Split Airport - LDSP',
      'Zadar Airport - LDZD', 'Zagreb Airport - LDZA', 'Riga Airport - EVRA', 'Kaunas Airport - EYKA', 'Vilnius Airport - EYVI', 'Luxemburg Airport - ELLX', 'Malta Airport - LMML', 'Chisinau Airport - LUKK',
      'Podgorica Airport - LYPG', 'Tivat Airport - LYTV', 'Amsterdam Airport Schiphol - EHAM', 'Eindhoven Airport - EHEH', 'Groningen Airport Eelde - EHGG', 'Lelystad Airport - EHLE', 'Maastricht Aachen Airport - EHBK',
      'Rotterdam The Hague Airport - EHRD', 'Skopje Airport - LWSK', 'Ålesund Airport - ENAL', 'Bergen Airport - ENBR', 'Bodø Airport - ENBO', 'Haugesund Airport - ENHD', 'Kristiansand Airport - ENCN', 'Oslo Airport - ENGM',
      'Sandefjord Airport Torp - ENTO', 'Stavanger Airport - ENZV', 'Tromsø Airport - ENTC', 'Trondheim Airport - ENVA', 'Charkov Airport - UKHH', 'Kiev Borispol Airport - UKBB', 'Kiev Zhuliany Airport - UKKK', 'Lviv Airport - UKLL',
      'Odessa Airport - UKOO', 'Graz Airport - LOWG', 'Innsbruck Airport - LOWI', 'Klagenfurt Airport - LOWK', 'Linz Airport - LOWL', 'Salzburg Airport - LOWS', 'Wenen Airport - LOWW', 'Gdansk Airport - EPGD', 'Katowice Airport - EPKT',
      'Krakau Airport - EPKK', 'Poznan Airport - EPPO', 'Szczecin-Goleniów Airport - EPSC', 'Warschau Airport - EPWA', 'Warschau Modlin Airport - EPMO', 'Wroclaw Airport - EPWR', 'Faro Airport - LPFR', 'Lissabon Airport - LPPT', 'Madeira Airport - LPMA',
      'Ponta Delgada Airport - LPPD', 'Porto Airport - LPPR', 'Boekarest Henri Coanda Airport - LROP', 'Cluj-Napoca Airport - LRCL', 'Iasi Airport - LRIA', 'Sibiu Airport - LRSB', 'Timisoara Airport - LRTR', 'Koltsovo Airport - USSS', 'Krasnodar Airport - URKK',
      'Moskou Domodedovo Airport - UUDD', 'Moskou Sheremetyevo Airport - UUEE', 'Moskou Vnukovo Airport - UUWW', 'Moskou Zhukovsky Airport - UUBW', 'Novosibirsk Tolmachevo Airport - UNNT', 'Sotsji Airport - URSS', 'St Petersburg Pulkovo Airport - ULLI',
      'Belgrado Nikola Tesla Airport - LYBE', 'Niš Airport - LYNI', 'Ljubljana Airport - LJLJ', 'Bratislava Airport - LZIB', 'Košice Airport - LZKZ', 'Alicante Airport - LEAL', 'Almeria Airport - LEAM', 'Asturias Airport - LEAS', 'Barcelona Airport - LEBL',
      'Bilbao Airport - LEBB', 'Fuerteventura Airport - GCFV', 'Girona Airport - LEGE', 'Gran Canaria Airport - GCLP', 'Granada-Jaén Airport - LEGR', 'Ibiza Airport - LEIB', 'Jerez Airport - LEJR', 'La Palma Airport - GCLA', 'Lanzarote Airport - GCRR',
      'Madrid Barajas Airport - LEMD', 'Malaga Airport - LEMG', 'Menorca Airport - LEMH', 'Palma de Mallorca Airport - LEPA', 'Región de Murcia Airport - LEMI', 'Reus Airport - LERS', 'Santander Airport - LEXJ', 'Santiago de Compostela Airport - LEST',
      'Sevilla Airport - LEZL', 'Tenerife North Airport - GCXO', 'Tenerife South Airport - GCTS', 'Valencia Airport - LEVC', 'Zaragoza Airport - LEZG', 'Brno Airport - LKTB', 'Praag Airport - LKPR', 'Adana Airport - LTAF', 'Ankara Esenboga Airport - LTAC',
      'Antalya Airport - LTAI', 'Dalaman Airport - LTBS', 'Istanbul Airport - LTFM', 'Istanbul Sabiha Gökcen Airport - LTFJ', 'Izmir Adnan Menderes Airport - LTBJ', 'Milas-Bodrum Airport - LTFE', 'Trabzon Airport - LTCG', 'Aberdeen Airport - EGPD',
      'Belfast City Airport - EGAC', 'Belfast International Airport - EGAA', 'Birmingham Airport - EGBB', 'Bristol Airport - EGGD', 'Cardiff Airport - EGFF', 'Doncaster Sheffield Airport - EGCN', 'East Midlands Airport - EGNX', 'Edinburgh Airport - EGPH',
      'Exeter Airport - EGTE', 'Glasgow Airport - EGPF', 'Glasgow Prestwick Airport - EGPK', 'Humberside Airport - EGNJ', 'Jersey Airport - EGJJ', 'Leeds Bradford Airport - EGNM', 'Liverpool Airport - EGGP', 'Londen City Airport - EGLC',
      'Londen Gatwick Airport - EGKK', 'Londen Heathrow Airport - EGLL', 'Londen Luton Airport - EGGW', 'Londen Southend Airport - EGMC', 'Londen Stansted Airport - EGSS', 'Manchester Airport - EGCC', 'Newcastle Airport - EGNT',
      'Southampton Airport - EGHI', 'Minsk Airport - UMMS', 'Göteborg Landvetter Airport - ESGG', 'Malmö Airport - ESMS', 'Stockholm Arlanda Airport - ESSA', 'Stockholm Bromma Airport - ESSB', 'Stockholm Skavsta Airport - ESKN',
      'Stockholm Västerås Airport - ESOW', 'Basel Mulhouse Freiburg Airport - LFSB', 'Bern Airport - LSZB', 'Genève Airport - LSGG', 'Zürich Airport - LSZH'],
      select: null,
      checkbox: false,
    }),

    methods: {
      calcStep1 () {
        if (this.$refs.form.validate()) {
          console.log('letsgo')
        } else {
          console.log('oh noe broke')
        }
      },
    },
  }
</script>
