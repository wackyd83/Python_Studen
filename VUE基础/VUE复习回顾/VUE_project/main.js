import Vue from 'vue'
import App from './App.vue'
//导入定义好的路由
import router from './router/router.js'
// 引入ElementUI
import ElementUI from 'element-ui'
// 引入css
import 'element-ui/lib/theme-chalk/index.css'
// 使用ElementUI
Vue.use(ElementUI)

new Vue({
    el:'#app',
    // 渲染单文件组件
    router,
    render:function(creater){
        return creater(App)
    }
})