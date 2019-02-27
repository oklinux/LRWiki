<template>
  <div class="listdoc">
      <router-link :to="{name:'docs',params:{docid :data.id}}">
      <span class="title">{{data.title}}</span>
      </router-link>
      <ul class='info'>
      <li>作者:{{data.author}}</li>
      <li>发表时间:{{data.create_time}}</li>
      </ul>
  </div>
</template>
<script>

export default {
  name:'WikiDoc',
  props:[
    'data',
  ]
}
</script>
<style>
.listdoc {
  display: block;
  margin-top: 1rem;
  margin-left: 2rem;
  text-align: left;
  border-bottom:1px solid rgba(178,186,194,.15);
  height: 4rem;
}
span.title{
  display: inline;
  margin: 0.5rem;
  font-size: 150%;
  font-weight: 500%;
  line-height: 120%;
}
ul.info{
  list-style: none;
}
.listdoc li{
  display: inline;
  margin: 0.5rem;
}

</style>
