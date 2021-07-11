
<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
      >
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="text-h6">
            Flight Prepper
          </v-list-item-title>
          <v-list-item-subtitle>
            Diamond DA40
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list
        dense
        nav
      >
        <v-list-item
          v-for="item in items"
          :key="item.title"
          :to="item.to"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
<!-- https://source.unsplash.com/collection/9855217/1600x900 -->
<v-app-bar
      app
      color="primary"
      dark
      shrink-on-scroll
      src="diamond1920.jpeg"
      scroll-target="#scrolling-techniques-2"
    >
      <template v-slot:img="{ props }">
        <v-img
          v-bind="props"
          gradient="to top right, rgba(19,84,122,.5), rgba(128,208,199,.8)"
        ></v-img>
      </template>

      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-app-bar-title>DA40 Flight Planner</v-app-bar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
  export default {
    data: () => ({ 
      drawer: null,
      items: [
          { title: 'Takeoff Distance', icon: 'mdi-airplane-takeoff', to: '/takeoff' },
          { title: 'My Plans', icon: 'mdi-view-list', to: '/myplans' },
          { title: 'About', icon: 'mdi-help-box', to: '/about'},
        ],
      }),
  }
</script>