<template>
  <section>
    <div class="remaining">Winners Count: {{ this.number }}</div>
    <div class="wrapper">
      <div id="names" class="names">{{ tempNames[0] }}</div>
    </div>
    <div class="wrapper wrapper2">
      <!-- <div id="gifts" class="names">{{ tempGift }}</div> -->
    </div>

    <v-dialog v-model="dialog" width="700">
      <v-card class="winner" height="700">
        <v-container fill-height>
          <v-row align="center">
            <v-col cols="12">
              <p class="infos">Winner</p>
              <p class="text">{{ winner[0] }}</p>
              <p class="infos">Gift</p>
              <p class="text">{{ winnerGift }}</p>
              <p class="infos">Mohallah</p>
              <p class="text">{{ winner[2] }}</p>
            </v-col>
          </v-row>
        </v-container>
      </v-card>
    </v-dialog>

    <v-dialog v-model="end" width="600">
      <v-card class="end" height="600"> </v-card>
    </v-dialog>
  </section>
</template>

<script>
import axios from "axios";

export default {
  name: "Ballot",
  data() {
    return {
      number: 0,
      tempNames: [],
      tempGift: null,
      names: [],
      namesGift: null,
      winner: [],
      winnerGift: null,
      show: true,
      dialog: false,
      end: false,
      entrants: [],
      gifts: [],
      finalList: [],
    };
  },
  methods: {
    randomName() {
      if (this.number == 51) {
        this.tempGift = "Smart Tablet";
      } else if (this.number == 52) {
        this.tempGift = "Gold Coin";
      } else {
        let rand2 = Math.floor(Math.random() * this.gifts.length);
        this.tempGift = this.gifts[rand2];
      }
      let rand = Math.floor(Math.random() * this.entrants.length);
      this.tempNames = this.entrants[rand];
    },

    rollClick() {
      if (this.number < 53) {
        this.show = false;
        let that = this;
        this.setDeceleratingTimeout(5, 30000);
        setTimeout(function () {
          that.winner = that.tempNames;
          that.winnerGift = that.tempGift;
          that.dialog = true;
          that.sendData(that.winner, that.winnerGift, that.number);
          that.finalList.push({
            index: that.number,
            name: that.winner[0],
            phoneNumber: that.winner[1],
            mohallah: that.winner[2],
            gift: that.winnerGift,
          });
          that.number = that.number + 1;
          let thiss = that;
          setTimeout(() => {
            thiss.resetCounter();
            thiss.dialog = false;
          }, 5000);
        }, 7000);
      } else {
        this.entrants = [];
        this.tempNames = [];
        this.tempGift = null;
        this.end = true;
        this.sendFinalListToServer();
      }
    },

    resetCounter() {
      this.names = [];
      this.namesGift = null;
      let index = this.entrants.indexOf(this.winner);
      let index2 = this.gifts.indexOf(this.winnerGift);
      if (index !== -1) {
        this.entrants.splice(index, 1);
      }
      if (index2 !== -1) {
        this.gifts.splice(index2, 1);
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

    getData() {
      axios.get("http://localhost:5000/data").then(
        (result) => {
          this.entrants = result.data.names.data;
          this.gifts = result.data.gifts;
          return;
        },
        (error) => {
          console.error(error);
          return;
        }
      );
    },

    sendData(winner, gift, index) {
      let data = { winner, gift, index };
      return data;
      // axios.post("http://localhost:5000/update", data);
    },

    sendFinalListToServer() {
      let data = { finalList: this.finalList };
      axios.post("http://localhost:5000/finalList", data);
      return;
    },
  },
  mounted() {
    this.getData();
  },
};
</script>

<style scoped>
.wrapper {
  width: 16%;
  position: fixed;
  text-align: center;
  top: 58%;
  left: 51%;
  transform: translate(-50%, -50%);
}
.wrapper2 {
  left: 59% !important;
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
.end {
  background-image: url("../assets/end.jpg");
  background-position: center;
  background-size: cover;
}
.text {
  font-size: 2.2rem;
  color: #4b6f79;
  text-align: center;
  z-index: 100;
}
.infos {
  font-size: 2rem;
  color: white;
  text-align: center;
}
.remaining {
  position: absolute;
  color: white;
  top: 208px;
  left: 155px;
  font-size: 2rem;
}
</style>
