<template>
<!-- eslint-disable max-len -->
   <button @click="downloadCSV" class="border border-blue-500 rounded-3xl h-12 px-4 bg-gradient-to-r from-red-500 to-blue-500 hover:opacity-80">
     <div class="inline-flex space-x-2 items-center h-full w-full">
       <img src="@/assets/download.svg" alt="download icon" />
       <p class="text-sm font-semibold text-white">
         Download CSV
       </p>
     </div>
   </button>
</template>

<script lang="ts">
import Vue from 'vue';
import axios from 'axios';
import FileDownload from 'js-file-download';

export default Vue.extend({
  name: 'DownloadCSVButton',
  props: {
    search_result: Array,
  },
  methods: {
    downloadCSV(): void {
      const data = {
        search_result: this.search_result,
      };
      axios
        .post('http://localhost:8000/download', data, { responseType: 'blob' })
        .then((response) => { FileDownload(response.data, 'BSE_data.csv'); });
    },
  },
});
</script>
