import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

const state = {
    messages: [],
};
const getters = {
    showMessages: (state) => state.messages,
};
const actions = {
    //async fetchMessages ({
    //commit
    //}) {
    //const response = await axios.get('https://dm.zuri.chat/api/v1/messages/6146cb29845b436ea04d1029')
    //commit('SET_ITEMS', response.data)
    //},
    //catch(error){
    //console.log(error)
    //}
    async fetchMessages({ commit }) {
        try {
            await axios
                .get(
                    'https://dm.zuri.chat/api/v1/messages/6146d126845b436ea04d102e'
                )
                .then((result) => {
                    console.log(result.data['results']);
                    commit('SET_ITEMS', result.data['results']);
                });
        } catch (error) {
            alert(error);
        }
    },
};
const mutations = {
    SET_ITEMS(state, messages) {
        state.messages = messages;
    },
};

export default {
    state,
    getters,
    actions,
    mutations,
};
