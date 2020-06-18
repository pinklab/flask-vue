import axios from 'axios';

const axiosObj = axios.create({
  baseURL: 'http://localhost:5000',
  timeout: 60 * 1000,
  headers: {
    'Content-Type': 'application/json',
  },
});

const VueAxiosPlugin = {
  install(Vue) {
    if (!Object.prototype.hasOwnProperty.call(Vue, '$axios')) {
      Object.defineProperty(Vue.prototype, '$axios', {
        get: function get() { return axiosObj; },
      });
    }
  },
};

export default VueAxiosPlugin;
