import Vue from 'vue';
import VueRouter from 'vue-router';
// import Home from '../views/Home.vue';
import Ping from '../components/Ping.vue';
import Tasks from '../components/Tasks.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Tasks',
    component: Tasks,
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
  },
  {
    path: '/ping',
    name: 'Ping',
    component: Ping,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
