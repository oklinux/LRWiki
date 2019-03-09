<template>
  <div id="app">
    <nav>
      <div class="nav-container row">
        <div class="nav-logo col-lg-offset-1 col-lg-2 col-sm-offset-1 col-sm-2">LinuxRen</div>
        <ul class="nav-links col-lg-5 col-sm-5">
          <li>
            <router-link to="/">Home</router-link>
          </li>
          <li>
            <a href="https://github.com/qomolinux/LRWiki" target="_blank">GitHub</a>
          </li>
          <li>
            <router-link to="/login" v-if="!islogin">login</router-link>
            <a v-if="islogin" @click='logout'>{{loginname}}</a>
          </li>
        </ul>
        <a
          class="mobile-menu-toggle col-lg-5 col-sm-offset-2 col-sm-2 col-xs-offset-2 col-xs-2"
          v-show="isshowtoggle"
          @click="isshowmenu=!isshowmenu;"
        ></a>
      </div>
      <div>
        <ul class="mobile-menu menu" v-show="isshowmenu">
          <li>
            <router-link to="/">Home</router-link>
          </li>
          <li>
            <a href="https://github.com/qomolinux/LRWiki" target="_blank">GitHub</a>
          </li>
          <li>
            <router-link to="/login" v-if="!islogin">login</router-link>
            <a v-if="islogin" @click='logout'>{{loginname}}</a>
          </li>
        </ul>
      </div>
    </nav>

    <router-view></router-view>
  </div>
</template>

<script>
import "mustard-ui";
export default {
  name: "app",
  components: {},
  computed:{
    islogin(){
      return this.$store.state.authentication.status.loggedIn;
    }
  },
  data() {
    return {
      isshowtoggle: true,
      isshowmenu: false,
      loginname:'',
    };
  },
  updated() {
    if (this.islogin){
      this.loginname = JSON.parse(localStorage.tokendata)['user_id']
    }
  },
  methods:{
    logout(){
      console.log('loggot');
      this.loginname=''
      this.$store.dispatch('authentication/logout')
    }
  }
};
</script>

<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
nav {
  padding: 0;
  margin: 0;
  position: relative;
}
.nav-container {
  max-width: 100%;
  padding: 0;
}
@media screen and(max-width: 576px) {
  .nav-logo {
    margin-left: 2rem;
    float: left;
  }
}
.mobile-menu {
  right: 10%;
  float: right;
  min-height: 100;
  position: absolute;
  z-index: 99;
}
</style>
