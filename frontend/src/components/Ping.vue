<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
export default {
  name: 'Ping',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    async get_pong() {
      const msg = await this.$axios.get('/api/v1/pong');
      this.msg = msg.data.msg;
    },
  },
  created() {
    this.get_pong();
  },

};
</script>
