<template>
  <div>
    <appHeader :propsdata="str" @renew="renewStr"></appHeader>
  </div>
</template>

<script>
import AppHeader from './components/AppHeader.vue'
export default{

  // new Vue({
  //   data:{
  //     str: 'hi'
  //   }
  // })
  /* 
     위와 같이 data를 객체로 선언해 주었는데,
     컴포넌트 동일한 값을 참조하면 안되기 때문에
     함수로 만들어서 객체를 return 해주어야한다.
  */

  data(){
    return{
      str: 'Header'
    }
  },

  components:{
    'appHeader': AppHeader
  },
  methods:{
    renewStr(){
      this.str = 'hi'
    }
  }
}
</script>

<style>

</style>