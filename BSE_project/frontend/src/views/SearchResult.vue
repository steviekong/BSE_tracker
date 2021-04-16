<template>
<!-- eslint-disable max-len -->
  <div class="w-full h-full justify-center items-center flex">
    <div class="w-3/5 h-3/5">
      <div>
        <p class="font-serif text-5xl text-pink-500">
          -1Dha
        </p>
        <p class="text-2xl">We actually pay you to invest</p>
      </div>
      <div class="w-full h-12 px-4 pt-3 rounded-2xl border-blue-500 border mt-8">
        <input class="outline-none w-full" type="text" for="search" id="search" v-model="search" placeholder="Company Name">
      </div>
      <button @click="onSearchClick" class="w-52 h-12 border bg-gradient-to-r from-purple-400 via-pink-500 to-red-500 rounded-lg text-white mt-10 text-xl font-sans hover:opacity-50">
        Search
      </button>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  name: 'Result',
  data() {
    return { search: '' };
  },
  methods: {
    onSearchClick() {
      this.$router.push(`/search/${this.search}`);
    },
  },
});
</script>
