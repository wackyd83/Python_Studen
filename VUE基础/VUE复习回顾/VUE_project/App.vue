<template>
    <div>单文件组件  {{ name }}
        <Child1></Child1>
        <Child2></Child2>
    </div>
</template>

<script>
import Child1 from './components/Child1.vue'
import Child2 from './components/Child2.vue'
export default{
    data:function(){
        return {name:'python'}
    },
    components:{
        Child1,
        Child2
    }
}
</script>

<style>
div{background-color: aquamarine;}
</style>