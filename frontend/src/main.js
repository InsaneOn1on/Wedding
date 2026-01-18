import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import './style.css'
import App from './App.vue'
import Home from './views/Home.vue'
import OurStory from './views/OurStory.vue'
import Schedule from './views/Schedule.vue'
import RSVP from './views/RSVP.vue'
import UpdateRSVP from './views/UpdateRSVP.vue'
import Admin from './views/Admin.vue'
import Registry from './views/Registry.vue'
import QA from './views/QA.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: Home },
    { path: '/our-story', component: OurStory },
    { path: '/schedule', component: Schedule },
    { path: '/rsvp', component: RSVP },
    { path: '/update-rsvp', component: UpdateRSVP },
    { path: '/admin', component: Admin },
    { path: '/registry', component: Registry },
    { path: '/qa', component: QA }
  ]
})

const app = createApp(App)
app.use(router)
app.mount('#app')
