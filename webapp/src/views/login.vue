<template>
  <div class="row">
    <div class="col col-lg-offset-3 col-lg-6 col-sm-offset-3 col-sm-6">
      <div class="card">
        <div class="form-control">
          <input v-model="username" type="text" placeholder="username">
        </div>
        <div class="form-control">
          <input v-model="password" type="password" placeholder="password">
        </div>
        <button class="button-primary button-purple" @click="_login()">Sign In</button>
      </div>
    </div>
  </div>
</template>

<script>
import {login} from '@/api/login.js'
export default {
  name: "viewlogin",
  data() {
      return {
          username:'',
          password:''
      }
  },
  methods:{
    _login(){
      console.log(this.password,this.username)
      // login(this.username,this.passwrod)
    }
  }
};
</script>
<style>
.card-title {
  color: black;
}
.card .form-control{
    margin: 10%;
}
.card{
  margin-top: 20%;
}
</style>