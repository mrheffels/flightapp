import Vue from 'vue'
import VueRouter from 'vue-router'
import TakeOff from '../views/TakeOff.vue'
import MyPlans from '../views/MyPlans.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/takeoff',
    name: 'TakeOff',
    component: TakeOff
  },
  {
    path: '/myplans',
    name: 'MyPlans',
    component: MyPlans
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
