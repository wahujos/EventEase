import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/Home.vue'
import Services from '../components/Services.vue'

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
  ]
})

export default router
