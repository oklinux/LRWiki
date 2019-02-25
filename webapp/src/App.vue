<template>
  <div id="app">
    <nav>
      <div class="nav-container row">
        <div class="nav-logo col-sm-2">
          LinuxRen
        </div>
        <ul class="nav-links">
          <li>
            <router-link to="/">Home</router-link>
          </li>
          <li>
            <a href="https://github.com/qomolinux/LRWiki" target="_blank">GitHub</a>
          </li>
          <li>
            <a href="/support">login</a>
          </li>
        </ul>
      </div>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
import 'mustard-ui'
export default {
  name: "app",
  components: {
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
</style>
