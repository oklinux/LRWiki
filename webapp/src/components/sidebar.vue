<template>
    <div class="sidebar sidebar-left col-lg-offset-1 col-lg-2 col-sm-offset-1 col-sm-2 col-xs-offset-1 col-xs-2">
        <h3 class="sidebar-category">介绍</h3>
        <ul class="sidebar-links">
            <li><a href="a">t1</a></li>
            <li><a href="a">t2</a></li>
        </ul>
        
    </div>
</template>

<script>
export default {
    name:'sidebar',
}
</script>
<style>
.sidebar{
    float: left;
    padding-left: 0;
}
@media screen and (max-width: 432px) {
  .sidebar {
      display: none;
  }
}

</style>
