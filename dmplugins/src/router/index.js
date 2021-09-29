import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import DMessage from '../components/allDmMessages.vue';

Vue.use(VueRouter);

const routes = [
    {
        path: '/dm',
        name: 'Home',
        component: Home,
    },
    {
        path: '/all-dm',
        name: 'DMessage',
        component: DMessage,
    },
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
});

export default router;
