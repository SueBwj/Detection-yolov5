<template>
  <div id="Footer">
    <p>{{ msg }}</p>
  </div>
</template>
<script>
export default {
  name: "AppFooter",
  data() {
    return {
      msg: "Group Member: Pqy Ljy Zjq Qyh Wj",
    };
  },
};
</script>
<style scoped>
#Footer {
  /*background:#F2F6FC;*/
  padding: 6px;
  border-radius: 5px;
  width: 80%;
  height: 80px;
  margin: 20px auto;
}

p {
  color: #d25a10;
  text-align: center;
  margin: 30px auto;
  font-size: 1.5em;
}
</style>
