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
        sendMsg:'',
        sender_id:'lkdl049052098509292',
        room_id:"61423bbc9fd1f4f655d445e7",
        allSentMsg:[],
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
        setSendMsg(state,payload){
            state.allSentMsg.push(payload)
        },
        setChat(state,newChat){
            state.sendMsg = newChat
        }
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
        async makeRequest({commit}){
            try {
                await apiServices.getClient(this.state.room_id,this.state.sender_id,this.state.sendMsg)
                .then(result => {
                    console.log(result.data)
                    commit('setSendMsg',result.data.data.message)
                })
            } catch (error) {
                alert(error)
            }
            this.state.sendMsg = ''    
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
        getSendMsg(state){
            return state.sendMsg;
        }
    },
    modules: {},

}
export default new Vuex.Store(store);
