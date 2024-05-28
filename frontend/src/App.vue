<template>
  <div id="app">
    <app-header></app-header>
    <app-content></app-content>
    <app-footer></app-footer>
  </div>
</template>

<script>
import AppContent from "./components/AppContent.vue";
import AppFooter from "./components/AppFooter.vue";
import AppHeader from "./components/AppHeader.vue";
export default {
  data() {
    return {};
  },
  components: {
    "app-header": AppHeader,
    "app-footer": AppFooter,
    "app-content": AppContent,
  },
  methods: {},
};
</script>

<style scope="this api replaced by slot-scope in 2.5.0+"></style>
