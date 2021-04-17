<template>
<!-- eslint-disable max-len -->
  <table class="table-fixed mx-2 md:mx-0 w-full md:w-8/12 text-left">
    <thead class="text-gray-600 font-bold text-lg border-b border-gray-300">
      <th class="w-4/12 p-r-4 py-4">
        Code
      </th>
      <th class="w-4/12">
        Name
      </th>
      <th class="w-4/12">
        Open
      </th>
      <th class="w-4/12">
        High
      </th>
      <th class="w-4/12">
        Low
      </th>
      <th class="w-4/12">
        Close
      </th>
    </thead>
    <tbody class="text-sm md:text-base">
      <tr v-for="item in rowData" v-bind:key="item.code" class="border-b border-gray-300">
        <td class="p-r-4 py-4">{{ item.Code }}</td>
        <td class="truncate">{{ item.Name }}</td>
        <td>{{ item.Open }}</td>
        <td>{{ item.High }}</td>
        <td>{{ item.Low }}</td>
        <td>{{ item.Close }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  name: 'Table',
  props: {
    rowData: Array,
  },
});
</script>
