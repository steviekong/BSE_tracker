<template>
<!-- eslint-disable max-len -->
   <div class="w-full h-12 pr-4 pl-14 pt-3 rounded-3xl border-blue-500 border relative">
      <input v-on:input="$emit('input', $event.target.value)" v-on:keyup.enter="$emit('search', $event.target.value)" class="outline-none w-full" type="text" for="search" id="search" v-model="search" placeholder="Company Name">
      <img class="w-6 h-6 absolute top-3 left-4" src="@/assets/icons8-search.svg" alt="search icon" />
    </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  name: 'SearchBar',
  data() {
    return { search: '' };
  },
});
</script>
