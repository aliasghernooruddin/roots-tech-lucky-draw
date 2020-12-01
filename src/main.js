import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';

import firebase from 'firebase';
require('firebase/firestore');

const config = {
  apiKey: "AIzaSyAT6trP8p10FSWiMznpiQ7hz3jAW9P3ZrU",
  authDomain: "roots-tech-lucky-draw.firebaseapp.com",
  databaseURL: "https://roots-tech-lucky-draw.firebaseio.com",
  projectId: "roots-tech-lucky-draw",
  storageBucket: "roots-tech-lucky-draw.appspot.com",
  messagingSenderId: "1098762318981",
  appId: "1:1098762318981:web:afd5bc55e5dcd6da9065ec",
  measurementId: "G-02D7KGYV5M"
};

firebase.initializeApp(config);

Vue.prototype.$firebase = firebase;

Vue.config.productionTip = false

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
