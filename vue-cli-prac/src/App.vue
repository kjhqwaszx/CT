<template>
  <form @submit="submitform">
    <div>
      <label for="username"> id: </label>
      <input id="username" type="text" v-model="username">
    </div>
    <div>
      <label for="password"> pw: </label>
      <input id="password" type="text" v-model="password">
    </div>
    <button type="submit">login</button>
  </form>
  
    
</template>
<script>
import axios from 'axios'
export default{
  data(){
    return{
      username:'',
      password:''
    }
  },
  methods: {
    submitform(event){
      event.preventDefault();
        console.log(this.username, this.password)
        var url = 'https://jsonplaceholder.typicode.com/users'

        var data = {
          username: this.username,
          password: this.password
        }
        axios.post(url,data)
          .then(function(response){
            console.log(response)
          })
          .catch(function(error){
            console.log(error)
          })
    }
  }
  
}
</script>
<style>

</style>