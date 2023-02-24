import Vue from 'vue'
import App from './App.vue'
//导入定义好的路由
import router from './router/router.js'

new Vue({
    el:'#app',
    // 渲染单文件组件
    router,
    render:function(creater){
        return creater(App)
    }
})