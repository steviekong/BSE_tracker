<template>
<!-- eslint-disable max-len -->
  <div class="w-full h-full justify-center items-center flex">
    <div class="md:w-3/5 h-3/5 w-4/5">
      <div>
        <p class="font-serif text-5xl text-pink-500">
          1dha
        </p>
        <p class="text-2xl">Search for the latest BSE Bhavcopy (Equity) data</p>
      </div>
      <div class="mt-8 w-3/4">
        <SearchBar @input="onInputChange" @search="onSearchClick"/>
      </div>
      <button @click="onSearchClick" class="w-52 h-12 border bg-gradient-to-r from-purple-400 via-pink-500 to-red-500 rounded-lg text-white mt-10 text-xl font-sans hover:opacity-50">
        Search
      </button>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import SearchBar from '@/components/SearchBar.vue';

export default Vue.extend({
  name: 'Home',
  data() {
    return {
      search: '',
    };
  },
  components: {
    SearchBar,
  },
  methods: {
    onSearchClick() {
      if (this.search !== '') {
        this.$router.push(`/search/${this.search}`);
      }
    },
    onInputChange(input: string) {
      this.search = input;
    },
  },
});
</script>
