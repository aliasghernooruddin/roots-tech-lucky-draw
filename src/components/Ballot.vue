<template>
  <section>
    <div class="wrapper">
      <div id="names" class="names" v-if="showName">{{ names[0] }}</div>
      <!-- <div class="winner">{{ winner }}</div> -->
    </div>
    <div class="wrapper2">
      <div class="names" id="gifts" v-if="showName">{{ namesGift }}</div>
      <!-- <div class="winner">{{ winnerGift }}</div> -->
    </div>

    <v-dialog v-model="dialog" width="500" class="winner">
      <v-card>
        <v-card-title class="headline">
          Use Google's location service?
        </v-card-title>
        <v-card-text {{winner}} {{winnerGift}}
          >Let Google help apps determine location. This means sending anonymous
          location data to Google, even when no apps are running.</v-card-text
        >
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" text @click="dialog = false">
            Disagree
          </v-btn>
          <v-btn color="green darken-1" text @click="dialog = false">
            Agree
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </section>
</template>

<script>
import $ from "jquery";
import axios from "axios";

export default {
  name: "Ballot",
  data() {
    return {
      show: true,
      dialog: false,
      names: [],
      namesGift: null,
      winner: null,
      winnerGift: null,
      showName: true,
      entrants: [],
      gifts: [
        "AirDots",
        "AirDots Pro",
        "Xbox",
        "PS5",
        "Handsfree",
        "Smartphone",
      ],
    };
  },
  methods: {
    randomName() {
      let rand = Math.floor(Math.random() * this.entrants.length);
      this.names = this.entrants[rand];

      let rand2 = Math.floor(Math.random() * this.gifts.length);
      this.namesGift = this.gifts[rand2];
    },

    rollClick() {
      this.show = false;
      let that = this;
      this.setDeceleratingTimeout(5, 30000);
      setTimeout(function () {
        that.winner = $("#names").text();
        that.winnerGift = $("#gifts").text();
        that.showName = false;
        that.dialog = true;
        let thiss = that;
        setTimeout(() => {
          thiss.resetCounter();
        }, 4000);
      }, 3000);
    },

    resetCounter() {
      this.showName = true;
      this.names = null;
      this.namesGift = null;
      let index = this.entrants.indexOf(this.winner);
      if (index !== -1) {
        this.entrants.splice(index, 1);
      }
      this.winner = null;
      this.winnerGift = null;
      this.rollClick();
    },

    setDeceleratingTimeout(factor, times) {
      let that = this;
      var internalCallback = (function (t, counter) {
        return function () {
          if (--t > 0) {
            window.setTimeout(internalCallback, ++counter * factor);
            that.randomName();
          }
        };
      })(times, 0);

      window.setTimeout(internalCallback, factor);
    },
  },
  mounted() {
    axios({
      method: "GET",
      url: "http://localhost:5000/data",
    }).then(
      (result) => {
        this.entrants = result.data.data;
      },
      (error) => {
        console.error(error);
      }
    );
  },
};
</script>


<style  scoped>
.wrapper {
  width: 21%;
  position: fixed;
  text-align: center;
  top: 60.2%;
  left: 38.5%;
  transform: translate(-50%, -50%);
}
.wrapper2 {
  width: 21%;
  position: fixed;
  text-align: center;
  top: 60.2%;
  left: 61%;
  transform: translate(-50%, -50%);
}
#roll {
  display: inline-block;
  font-size: 4rem;
  background: none;
  border: none;
  outline: none;
  transition: 400ms ease-in-out;
}
.names {
  display: inline-block;
  background: none;
  border: none;
  outline: none;
  transition: 400ms ease-in-out;
  font-size: 2.5rem;
}
.winner {
  display: inline-block;
  font-size: 5rem;
  color: #fbcf26;
  background: none;
  border: none;
  outline: none;
  transition: 400ms ease-in-out;
  background-image: url("../assets/winner.jpg");
  height: 100%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
</style>