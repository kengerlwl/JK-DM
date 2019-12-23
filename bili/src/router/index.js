import Vue from 'vue'
import Router from 'vue-router'
import playMv from '@/page/playMv'
import main from '@/page/main'
import login from '@/page/login'
import register from '@/page/register'
import home_test from '@/page/home_test'

Vue.use(Router)

export default new Router({
    routes: [{
            path: '/play',
            name: 'playMv',
            component: playMv
        },
        {
            path: '/',
            name: 'login',
            component: login
        },
        {
            path: '/hometest',
            name: 'home_test',
            component: home_test
        },
        {
            path: '/main',
            name: 'main',
            component: main
        },
        {
            path: '/login',
            name: 'login',
            component: login
        },
        {
            path: '/register',
            name: 'register',
            component: register
        },
    ]
})