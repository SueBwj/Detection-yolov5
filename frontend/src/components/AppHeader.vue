<template>
  <!-- As a heading -->
  <nav class="navbar bg-body-tertiary">
    <div class="container-fluid">
      <span><i style="font-size: 23px">🍎🍊🍌</i></span>
      <span class="navbar-brand mb-0 h1 text-danger">{{ msg }}</span>
    </div>
  </nav>
  <div id="Header">
    <div class="top-left-edition">
      <span> </span>
    </div>
  </div>
</template>
<script>
export default {
  name: "AppHeader",
  data() {
    return {
      msg: "YOLOv5-Fruit-Detection",
      activeIndex: "1",
    };
  },
  methods: {},
};
</script>
<style scoped></style>
