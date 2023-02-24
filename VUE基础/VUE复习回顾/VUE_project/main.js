import Vue from 'vue'
import App from './App.vue'

new Vue({
    el:'#app',
    // 渲染单文件组件
    render:function(create){
        return create(App)
    }
})