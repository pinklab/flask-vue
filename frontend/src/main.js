import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import axiosPlugin from './plugins/axios';

Vue.use(axiosPlugin);
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
