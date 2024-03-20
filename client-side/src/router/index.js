import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/Home.vue'
import Services from '../components/Services.vue'
import SignUp from '../components/SignUp.vue'
import Caterers from '../components/Caterers.vue'
import Equipment from '../components/Equipment.vue'
import Emcees from '../components/Emcees.vue'
import Artists from '../components/Artists.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/services',
      name: 'services',
      component: Services
    },
    {
      path: '/register',
      name: 'signup',
      component: SignUp
    },
    {
      path: '/services/caterers',
      name: 'caterers',
      component: Caterers
    },
    {
      path: '/services/equipment',
      name: 'equipment',
      component: Equipment
    },
    {
      path: '/services/emcees',
      name: 'emcees',
      component: Emcees
    },
    {
      path: '/services/artists',
      name: 'artists',
      component: Artists
    }
  ]
})

export default router
