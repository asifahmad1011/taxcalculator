<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <div class="d-flex align-center">Tax Calculator</div>
    </v-app-bar>

    <v-main>
      <TaxCalculator />
    </v-main>
  </v-app>
</template>

<script lang="ts">
import Vue from "vue";
import TaxCalculator from "./components/TaxCalculator.vue";

export default Vue.extend({
  name: "App",

  components: {
    TaxCalculator,
  },

  data: () => ({
    //
  }),
});
</script>
