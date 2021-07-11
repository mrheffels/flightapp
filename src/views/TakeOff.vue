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
        :counter="5"
        :rules="bagageRules"
        label="Bagage in Kg"
        required
      ></v-text-field>
      <v-text-field
        v-model="paxAmount"
        :counter="1"
        :rules="paxRules"
        label="Pax Amount"
        required
      ></v-text-field>
      <v-text-field
        v-model="windComponent"
        :counter="2"
        :rules="windRules"
        label="Wind component"
        required
      ></v-text-field>
      <v-text-field
        v-model="fuel"
        :counter="1"
        :rules="fuelRules"
        label="Fuel in USgal"
        required
      ></v-text-field>
      <v-checkbox
        v-model="checkbox"
        :rules="[v => !!v || 'You must agree to continue!']"
        label="Are you a battieboy?"
        required
      ></v-checkbox>

      <v-btn
        :disabled="!valid"
        color="success"
        class="mr-4"
        @click="validate"
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
      valid: true,
      airport: '',
      pressAlt: 0,
      temperature: 0,
      fuel: 0,
      bagage: 0,
      paxAmount: 1,
      windComponent: 0,
      name: '',
      pressAltRules: [
        v => !!v || 'Pressure Altitude is required',
        v => (v || '').length <= 5 || 'Pressure Altitude has max 5 digits',
        v => (v && /^\d+$/.test(v)) || 'Pressure Altitude can only contain positive numbers',
      ],
      fuelRules: [
        v => !!v || 'Fuel is required',
        v => (v || '').length <= 2 || 'Fuel has max 2 digits',
        v => (v && /^\d+$/.test(v)) || 'Fuel can only contain positive numbers',
      ],
      bagageRules: [
        v => !!v || 'Bagage is required',
        v => (v || '').length <= 2 || 'Bagage has max 2 digits',
        v => (v && /^\d+$/.test(v)) || 'Bagage can only contain positive numbers',
      ],
      paxRules: [
        v => !!v || 'Pax Amount is required',
        v => (v || '').length <= 1 || 'Pax Amount has max 1 digit',
        v => (v && /^\d+$/.test(v)) || 'Pax Amount can only contain positive numbers',
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
      airports: ['LATI', 'UDYZ', 'UBBB', 'EBAW', 'EBBR', 'EBCI', 'EBLG', 'EBOS',
      'LQSA', 'LQTZ', 'LBBG', 'LBSF', 'LBWN', 'LCLK', 'LCPH', 'EKYT', 'EKAH', 'EKBI',
      'EKCH', 'EKVG', 'EDJA', 'EDDB', 'EDDW', 'EDLW', 'EDDC', 'EDDL', 'EDDF', 'EDFH',
      'EDNY', 'EDDH', 'EDDV', 'EDSB', 'EDDK', 'EDDP', 'EDDM', 'EDDG', 'EDDN', 'EDLP',
      'EDDS', 'EDLV', 'EETN', 'EFHK', 'EFOU', 'EFRO', 'EFTP', 'EFTU', 'EFVA', 'LFKJ',
      'LFKB', 'LFBE', 'LFBZ', 'LFBD', 'LFRB', 'LFKF', 'LFQQ', 'LFLL', 'LFML', 'LFMT',
      'LFRS', 'LFMN', 'LFOB', 'LFPG', 'LFPO', 'LFRN', 'FMEE', 'LFST', 'LFTH', 'LFBO',
      'UGKO', 'UGTB', 'LGAV', 'LGSA', 'LGKR', 'LGIR', 'LGKO', 'LGMK', 'LGRP', 'LGSR',
      'LGTS', 'LGZA', 'LHBP', 'LHDC', 'EICK', 'EIDW', 'EIKN', 'EIKY', 'EINN', 'BIKF',
      'LIEA', 'LIPY', 'LIBD', 'LIME', 'LIPE', 'LIBR', 'LIEE', 'LICC', 'LICB', 'LIRQ',
      'LIMJ', 'LICA', 'LIML', 'LIMC', 'LIRN', 'LIEO', 'LICJ', 'LIRZ', 'LIBP', 'LIRP',
      'LIRA', 'LIRF', 'LICT', 'LIPH', 'LIPQ', 'LIMF', 'LIPZ', 'LIPX', 'UAAA', 'UACC',
      'BKPR', 'LDDU', 'LDPL', 'LDSP', 'LDZD', 'LDZA', 'EVRA', 'EYKA', 'EYVI', 'ELLX',
      'LMML', 'LUKK', 'LYPG', 'LYTV', 'EHAM', 'EHEH', 'EHGG', 'EHLE', 'EHBK', 'EHRD',
      'LWSK', 'ENAL', 'ENBR', 'ENBO', 'ENHD', 'ENCN', 'ENGM', 'ENTO', 'ENZV', 'ENTC',
      'ENVA', 'UKHH', 'UKBB', 'UKKK', 'UKLL', 'UKOO', 'LOWG', 'LOWI', 'LOWK', 'LOWL',
      'LOWS', 'LOWW', 'EPGD', 'EPKT', 'EPKK', 'EPPO', 'EPSC', 'EPWA', 'EPMO', 'EPWR',
      'LPFR', 'LPPT', 'LPMA', 'LPPD', 'LPPR', 'LROP', 'LRCL', 'LRIA', 'LRSB', 'LRTR',
      'USSS', 'URKK', 'UUDD', 'UUEE', 'UUWW', 'UUBW', 'UNNT', 'URSS', 'ULLI', 'LYBE',
      'LYNI', 'LJLJ', 'LZIB', 'LZKZ', 'LEAL', 'LEAM', 'LEAS', 'LEBL', 'LEBB', 'GCFV',
      'LEGE', 'GCLP', 'LEGR', 'LEIB', 'LEJR', 'GCLA', 'GCRR', 'LEMD', 'LEMG', 'LEMH',
      'LEPA', 'LEMI', 'LERS', 'LEXJ', 'LEST', 'LEZL', 'GCXO', 'GCTS', 'LEVC', 'LEZG',
      'LKTB', 'LKPR', 'LTAF', 'LTAC', 'LTAI', 'LTBS', 'LTFM', 'LTFJ', 'LTBJ', 'LTFE',
      'LTCG', 'EGPD', 'EGAC', 'EGAA', 'EGBB', 'EGGD', 'EGFF', 'EGCN', 'EGNX', 'EGPH',
      'EGTE', 'EGPF', 'EGPK', 'EGNJ', 'EGJJ', 'EGNM', 'EGGP', 'EGLC', 'EGKK', 'EGLL',
      'EGGW', 'EGMC', 'EGSS', 'EGCC', 'EGNT', 'EGHI', 'UMMS', 'ESGG', 'ESMS', 'ESSA',
      'ESSB', 'ESKN', 'ESOW', 'LFSB', 'LSZB', 'LSGG', 'LSZH'],

      select: null,
      checkbox: false,
    }),

    methods: {
      validate () {
        this.$refs.form.validate()
      },
    },
  }
</script>
