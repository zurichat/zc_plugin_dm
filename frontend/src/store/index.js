import Vue from 'vue';
import Vuex from 'vuex';
import apiServices from '../services/apiServices.js';

Vue.use(Vuex);
const store = {
    state: {
        pickEmoji: false,
        showReply: false,
        emojis: [],
        emojiSet: Object.create(null),
    },
    mutations: {
        setPickEmoji(state, payload) {
            state.pickEmoji = payload;
        },
        setShowReply(state, payload) {
            state.showReply = payload;
        },
        setEmojis(state, payload) {
            state.emojis = payload;
        },
        setEmojiSet(state, payload) {
            state.emojiSet = payload;
        },
    },
    actions: {
        setEmojis({ commit, state }, payload) {
            const emojis = [...state.emojis, payload];
            commit('setEmojis', emojis);
            const map = emojis.reduce(
                (prev, next) => ({
                    ...prev,
                    [next]: (prev[next] || 0) + 1,
                }),
            );
            commit('setEmojiSet', map);
        },
        //making API call to the backend:deveeb
        async makeRequest(){
            try {
              await apiServices.getClient()
              .then(result => {
                console.log(result.data)
              })
            } catch (error) {
              alert(error)
            }
        }
    },
    getters: {
        pickEmoji(state) {
            return state.pickEmoji;
        },
        showReply(state) {
            return state.showReply;
        },
        emojis(state) {
            return state.emojis;
        },
        emojiSet(state) {
            return state.emojiSet;
        },
    },
    modules: {},

}
export default new Vuex.Store(store);
