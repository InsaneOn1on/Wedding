import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import './style.css'
import App from './App.vue'
import Home from './views/Home.vue'
import RSVP from './views/RSVP.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: Home },
    { path: '/rsvp', component: RSVP }
  ]
})

const app = createApp(App)
app.use(router)
app.mount('#app')
