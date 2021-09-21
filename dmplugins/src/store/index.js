import Vue from 'vue';
import Vuex from 'vuex';
import apiServices from '../services/apiServices';
import messages from './modules/messages'


Vue.use(Vuex);
const store = {
    state: {
        pickEmoji: false,
        showReply: false,
        emojis: [],
        emojiSet: Object.create(null),
        sendMsg:'',
        recieveMsg:[],
        sender_id:'6146ce37845b436ea04d102d',
        room_id:"6146d126845b436ea04d102e",
        message_id: "6146d432845b436ea04d103b",
        allSentMsg:[ ],
        // For Reply Thread
        showReplyThread: false,
        replyThreadMsgs: {
            username: 'Sandra Bernard',
            userImg: '',
            clickedMsg: 'Clicked messages will be shown here when a user wants to reply in a thread. Thank you',
            senderId: '6145fc9a285e4a18402074f4',
            replyThreadNewMsg: [ ]
        }
    },
    mutations: {
        setPickEmoji(state, payload) {
            state.pickEmoji = payload;
        },
        setShowReply(state, payload) {
            state.showReply = payload;
        },
        addEmojis(state, payload) {
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
        },
        setReceiveMsg(state,newMsg){
            state.recieveMsg = newMsg
        }
    },
    actions: {
        addEmojis({ commit, state }, payload) {
            const emojis = [...state.emojis, payload];
            commit('addEmojis', emojis);
            const emojiCount = emojis.reduce((prev, value) => ({
                ...prev,
                [value]: (prev[value] || 0) + 1
            }), {});
            commit('setEmojiSet', emojiCount);

            // apiServices.postEmoji("6146cb29845b436ea04d1029",this.state.message_id, payload)
            // .then(result => {
            //     console.log(result.data)
            // })
        },
        async fetchEmojis({commit}){
            try{
                await apiServices.getEmojis("6146cb29845b436ea04d1029",this.state.message_id)
                .then(result =>{
                    console.log(result.data)
                    // commit('addEmojis', result.data)
                })   
            } catch (error){
                console.log(error)
            }
        },
        //making API call to the backend:deveeb
        async makeRequest({commit}){
            try {
                await apiServices.getClient(this.state.room_id,this.state.sender_id,this.state.sendMsg)
                .then(result => {
                    //console.log(result.data)
                    commit('setSendMsg',result.data.data.message)
                })
            } catch (error) {
                alert(error)
            }
            this.state.sendMsg = ''    
        },
        //getting messages in room
        async getRequest({commit}){
            try {
                await apiServices.recieveClient(this.state.room_id)
                .then(result => {
                    console.log(result.data.results)
                    commit('setReceiveMsg',result.data.results)
                })
            } catch (error) {
                alert(error)
            }   
        },
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
        },
        getRecieveMsg(state){
            return state.recieveMsg
        }
    },
    modules: {
        messages,
    },
};
export default new Vuex.Store(store);
