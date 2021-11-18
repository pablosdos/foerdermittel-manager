// Filters & Programs

/* eslint-disable */
import axios from 'axios'
/* eslint-enable */
import * as Filters from '~/helpers/filters'

const logCounter = false

export const state = () => ({
  programs: [],
  filteredPrograms: [],
  lengthOfFilteredPrograms: '',
  program: {},
  detailProgram: {},
  filter: {
    search: '',
    region: 'Alle',
    theme: 'Alle',
    type: 'Alle',
    order: 'name'
  }
})

export const getters = {

}

export const actions = {
  // Load all programs at Pageload
  // async getPrograms ({ commit }) {
  // nuxtServerInit MUSS IN index.js SEIN
  async nuxtServerInit ({ commit, dispatch }, { req, res }) {
    // const programs = await this.$axios.$get('http://bh-admin.paul-kluge.de//api/programs/')
    const programs = await this.$axios.$get('http://127.0.0.1:4000/api/programs/')
    if (logCounter) {
      console.log('ANZAHL ALLER FÖRDERMITTEL (index.js)')
      console.log(programs)
      console.log(programs.length)
    }
    const filteredPrograms = programs
    commit('addPrograms', programs)
    commit('addFilteredPrograms', filteredPrograms)
    // dispatch('filterPrograms')
    return programs
  },
  async filterOrder ({ commit }, order) {
    await commit('setProgram', order)
    await commit('orderPrograms')
  },
  async setDetailProgram ({ commit, dispatch }, program) {
    await commit('setDetailProgram', program)
  },
  async filterStatus ({ commit, dispatch }, status) {
    await commit('setFilterStatus', status)
    dispatch('filterPrograms')
  },
  async filterTheme ({ commit, dispatch }, status) {
    await commit('setThemeStatus', status)
    dispatch('filterPrograms')
  },
  async filterType ({ commit, dispatch }, status) {
    await commit('setTypeStatus', status)
    dispatch('filterPrograms')
  },
  async filterSearch ({ commit, dispatch }, search) {
    await commit('setFilterSearch', search)
    dispatch('filterPrograms')
  },
  async filterPrograms ({ commit }) {
    await commit('filterPrograms')
    await commit('orderPrograms')
  }
}

export const mutations = {
  setDetailProgram (state, detailProgram) { state.detailProgram = detailProgram },
  setFilterStatus (state, region) { state.filter.region = region },
  setThemeStatus (state, theme) { state.filter.theme = theme },
  setTypeStatus (state, type) { state.filter.type = type },
  setFilterSearch (state, search) { state.filter.search = search },
  setOrder (state, order) { state.filter.order = order },

  filterPrograms (state) {
    const programs = [...state.programs]
    state.filteredPrograms = programs
    state.filteredPrograms = Filters.filterPrograms(state.filter, programs)
    state.lengthOfFilteredPrograms = Object.keys(state.filteredPrograms[0]).length

    // state.lengthOfFilteredPrograms = 5
  },
  orderPrograms (state) {
    const programs = [...state.filteredPrograms]
    state.filteredPrograms = Filters.orderPrograms(state.filter.order, programs)
  },
  // die JSON-Response wird auf den Zustand gemapt.
  addPrograms (state, programs) {
    state.programs.push({ ...programs })
  },
  addFilteredPrograms (state, filteredPrograms) {
    state.filteredPrograms.push({ ...filteredPrograms })
    state.lengthOfFilteredPrograms = Object.keys(state.filteredPrograms[0]).length
  }
}
