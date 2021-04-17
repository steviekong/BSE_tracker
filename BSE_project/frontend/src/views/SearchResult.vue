<template>
<!-- eslint-disable max-len -->
  <div class="w-full justify-left flex flex-col">
    <header class="p-4 shadow-lg">
      <div class="flex flex-col w-full">
        <div>
          <router-link to="/">
            <p class="font-serif text-3xl text-pink-500 font-bold w-8">
              1Dha
            </p>
          </router-link>
        </div>
        <div class="w-full md:w-1/2 mt-4">
          <SearchBar @input="onInputChange" @search="onSearchClick" v-bind:placeholder="this.$route.params.searchResult"/>
        </div>
      </div>
    </header>
    <div class="w-full flex flex-col items-center mt-8">
      <div class="inline-flex items-center space-x-8">
        <h2 class="text-base md:text-2xl py-6 font-medium font-mono">BSE Bhavcopy (Equity) for {{ date }}</h2>
        <DownloadCSVButton  v-bind:search_result="search_result" />
      </div>
      <div class="md:w-full flex justify-center">
        <Table v-if="search_result !== null && search_result.length > 0" :rowData="search_result" />
        <div v-if="search_result === null">
          <img class="w-24 h-24" src="@/assets/loading.svg" alt="loading" />
        </div>
        <div v-if="search_result !== null && search_result.length <= 0">
          <h3 class="text text-red-500 py-6 font-medium font-mono">No results found for that search query</h3>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import axios from 'axios';
import Table from '@/components/Table.vue';
import SearchBar from '@/components/SearchBar.vue';
import DownloadCSVButton from '@/components/DownloadCSVButton.vue';
import dayjs from 'dayjs';

export default Vue.extend({
  name: 'Result',
  data() {
    return {
      search_result: null,
      date: dayjs().format('YYYY-MM-DD'),
      search: '',
    };
  },
  mounted() {
    if (this.search_result === null) {
      this.searchQuery();
    }
  },
  components: {
    Table,
    SearchBar,
    DownloadCSVButton,
  },
  methods: {
    onSearchClick() {
      if (this.search !== '') {
        this.$router.push(`/search/${this.search}`);
        this.searchQuery();
      }
    },
    onInputChange(input: string) {
      this.search = input;
    },
    searchQuery() {
      axios
        .get('http://localhost:8000/search', {
          params: {
            search_string: this.$route.params.searchResult,
          },
        })
        .then((response) => { (this.search_result = response.data.search_result); });
    },
  },
});
</script>
