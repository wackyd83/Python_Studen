import Vue from 'vue'
import Router from 'vue-router'
import Child1 from '../components/Child1.vue'
import Child2 from '../components/Child2.vue'

// 指定Vue使用路由
Vue.use(Router)
// 指定路由规则
export default new Router({
    // 定义匹配规则
   routes:[
       {
           path:'/child1',  // 匹配根路径／，加载Chiled1中的内容
           component:Child1
       },
       {
           path:'/child2',
           component:Child2
       }
   ]
})


