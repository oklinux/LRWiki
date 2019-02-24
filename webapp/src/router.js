import Vue from 'vue'
import Router from 'vue-router'
import wikidocs from './views/wikidocs.vue'
Vue.use(Router)
let base =`${process.env.BASE_URL}`
export default new Router({
  mode : 'history',
  base : base,
  routes: [
    {
      path: '/',
      name: 'home',
      component: wikidocs,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    },
    {
      path: '/docs/:docid',
      name: 'docs' ,
      props: true ,
      component: () => import('./components/DocDetail.vue')
    }
  ]
})
