<template>
    <div>
        <header>
            <h1>{{propsdata}}</h1>
            <button @click="sendEvent">send</button>
        </header>
    </div>
</template>

<script>
export default{
    data(){
        return{
            str: 'AppHeader'
        }
    },
    props:['propsdata'],
    methods:{
        sendEvent(){
            this.$emit('renew')
        }
    }
}
</script>

<style>

</style>