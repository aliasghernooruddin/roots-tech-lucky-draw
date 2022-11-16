import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';

import firebase from 'firebase';
require('firebase/firestore');

const config = {
  apiKey: "",
  authDomain: "",
  databaseURL: "",
  projectId: "",
  storageBucket: "",
  messagingSenderId: "",
  appId: "",
  measurementId: ""
};

firebase.initializeApp(config);

Vue.prototype.$firebase = firebase;

Vue.config.productionTip = false

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
