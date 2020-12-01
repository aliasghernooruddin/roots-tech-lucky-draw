<template>
  <v-app >
    <div id="apps" @click="rollClick()">
    <Ballot ref="ballotComponent" /></div>
  </v-app>
</template>

<script>
import Ballot from "./components/Ballot.vue";

export default {
  name: "App",
  components: {
    Ballot,
  },
  methods: {
    rollClick() {
      console.log("asd");
      this.$refs.ballotComponent.rollClick();
    },
  },
};
</script>

<style>
#apps {
  background-image: url("assets/bg.jpg");
  height: 100%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
</style>
