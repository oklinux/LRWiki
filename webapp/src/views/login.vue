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
export default {
  name: "viewlogin",
  data() {
      return {
          username:'',
          password:'',
          submitted: false
      }
  },
  computed:{
    loggingIn(){
      return this.$store.state.authentication.status.loggingIn;
    }
  },
  methods:{
    _login(){
      console.log(this.username,this.password)
      this.submitted=true
      const {username,password} =this
      const { dispatch } = this.$store;
      if (username&&password){
        dispatch('authentication/login',{username,password})
      }

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