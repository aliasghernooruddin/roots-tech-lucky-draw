<template>
  <section>
    <div class="wrapper">
      <div id="names" class="names" v-if="showName">{{ names[0] }}</div>
    </div>
    <div class="wrapper wrapper2">
      <div id="gifts" class="names" v-if="showName">{{ namesGift }}</div>
    </div>

    <v-dialog v-model="dialog" width="600">
      <v-card class="winner" height="600">
        <v-container fill-height>
          <v-row align="center" >
            <v-col cols="12">
              <p class="infos">Winner</p>
              <p class="text">{{ winner }}</p>
              <p class="infos">Gift</p>
              <p class="text">{{ winnerGift }}</p>
            </v-col>
          </v-row>
        </v-container>
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
      winner: "Aliasgher Ahmedabawala",
      winnerGift: "Iphone Airpods",
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
          console.log(thiss.winner, thiss.winnerGift)
          thiss.resetCounter();
          thiss.dialog = false;
        }, 4000);
      }, 3000);
    },

    resetCounter() {
      this.showName = true;
      this.names = [];
      this.namesGift = null;
      let index = this.entrants.indexOf(this.winner);
      if (index !== -1) {
        this.entrants.splice(index, 1);
      }
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
  top: 54%;
  left: 38.5%;
  transform: translate(-50%, -50%);
}
.wrapper2 {
  left: 61% !important;
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
  font-size: 20px;
}
.winner {
  background-image: url("../assets/winner.jpg");
  background-position: center;
  background-size: cover;
}
.text {
  font-size: 3.2rem;
  color: #fed630;
  text-align: center;
}
.infos {
  font-size: 2rem;
  color: white;
  text-align: center;
}
</style>