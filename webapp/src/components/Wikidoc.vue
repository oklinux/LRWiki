<template>
  <div>
      <router-link :to="{path:'docs',params:{docid :'data.id'}}">
      {{data.title}}
      </router-link>
      {{data.create_time}},
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