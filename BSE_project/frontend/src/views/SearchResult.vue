<template>
<!-- eslint-disable max-len -->
  <div class="w-full h-full justify-center text-center mt-8 flex">
    <div class="w-3/5 h-3/5">
      <div>
        <p class="font-serif text-5xl text-pink-500">
          -1Dha
        </p>
        <p class="text-2xl">We actually pay you to invest</p>
      </div>
      <div>
      <p> {{ info }} </p>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import axios from 'axios';

export default Vue.extend({
  name: 'Result',
  data() {
    return {
      info: null,
    };
  },
  mounted() {
    axios
      .get('http://localhost:8000/search', {
        params: {
          search_string: 'S',
        },
      })
      .then((response) => { (this.info = response); });
  },
});
</script>
