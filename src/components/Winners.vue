
<template>
  <section>
    <v-container fill-height>
      <v-row align="center" justify="center">
        <v-col cols="12" md="9">
          <v-img src="../assets/logo.png" aspect-ratio="6" contain></v-img>
          <br /><br />
          <h1 v-if="winnersList.length != 0" class="winners">Winners List</h1>
          <ul class="down">
            <li
              :key="item.index"
              v-for="item in winnersList"
              class="items"
              :class="[$vuetify.breakpoint.mdAndUp ? 'text-h5' : 'text-body-1']"
            >
              {{ item.index + 1 }}) {{ item["winner"][0] }} - {{ item["gift"] }}
            </li>
          </ul>
        </v-col>
      </v-row>
    </v-container>
    <v-footer absolute class="font-weight-medium footer">
      <v-col class="text-center footer" cols="12">
        Copyrights &#169;
        <a
          class="footer"
          target="_blank"
          href="https://www.instagram.com/rootstechpakistan/"
        >
          <strong>Roots Tech </strong></a
        >
        <br />
        Designed & Developed by
        <a class="footer" target="_blank" href="https://webnapps.imfast.io">
          <strong>Aliasgher Nooruddin</strong></a
        >
      </v-col>
    </v-footer>
  </section>
</template>

<script>
export default {
  name: "Winners",
  data() {
    return {
      winnersList: [],
    };
  },
  mounted() {
    const db = this.$firebase.firestore();
    db.collection("winners")
      .orderBy("index", "asc")
      .onSnapshot((querySnapshot) => {
        const winnersList = [];
        querySnapshot.forEach((doc) => {
          winnersList.push(doc.data());
        });
        this.winnersList = winnersList;
      });
  },
};
</script>

<style lang="scss">
.winners {
  color: white;
  font-size: 40px;
  text-align: center;
}

.items {
  color: white;
  font-size: 30px;
  text-transform: uppercase;
  margin-bottom: 10px;
}

.footer {
  background: none !important;
  color: white !important;
  text-decoration: none;
}

.down {
  list-style-type: none;
  margin-bottom: 65px;
}
</style>