import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  //  components:{
  //   'app':App
  // } 동일한 내용
}).$mount('#app')   
// el: '#app' 동일한 내용
