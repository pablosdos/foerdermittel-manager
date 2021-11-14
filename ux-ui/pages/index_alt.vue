<template>
  <div>
    <!--   <select v-model="selected">
      <option disabled value="">
        Please select one
      </option>
      <option>Bayern</option>
      <option>Rheinland-Pfalz</option>
      <option>Hessen</option>
    </select>
    Input
   <input v-model="'getFil"> -->
    <div>
      <button @click="getFilters">BUTTON</button>
    </div>
    <ul v-for="filter in filters[0]" :key="filter.title">
      <li>{{ filter.name }}</li>
    </ul>
  </div>
</template>

<script>
// import {mapState, mapGetters, mapMutations} from 'vuex'
import { mapState, mapActions } from 'vuex'

export default {
  computed: mapState(['filters']),
  methods: {
    ...mapActions(['getFilters'])
  }
}
</script>
