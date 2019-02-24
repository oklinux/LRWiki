<template>
  <div id="app">
    <WikiTitle/>
    <nav>
      <div class="nav-container">
        <div class="nav-logo">
          LinuxRen
        </div>
        <ul class="nav-links">
          <li>
            <router-link to="/">Home</router-link>
          </li>
          <li>
            <a href="https://github.com/kylelogue/mustard-ui" target="_blank">GitHub</a>
          </li>
          <li>
            <a href="/support">Support</a>
          </li>
        </ul>
      </div>
    </nav>
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
