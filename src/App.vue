<template>
  <v-app>
    <!-- <div id="apps"> -->
    <div id="apps" @click="rollClick()">
      <!-- <Winners /> -->
      <Ballot ref="ballotComponent" />
    </div>
  </v-app>
</template>

<script>
import Ballot from "./components/Ballot.vue";
// import Winners from "./components/Winners.vue";

export default {
  name: "App",
  components: {
    Ballot,
    // Winners,
  },
  methods: {
    rollClick() {
      this.$refs.ballotComponent.rollClick();
    },
  },
};
</script>

<style>
#apps {
  background-image: url("assets/background.jpg");
  /* background-image: url("assets/bg1.jpg"); */
  height: 100%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
</style>
