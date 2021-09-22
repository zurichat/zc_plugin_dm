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
        async addEmojis({ commit }, payload) {
            const created = new Date().toISOString();
            const newEmoji = {
                aliases: [payload.name],
                message_id: this.state.message_id,
                sender_id: this.state.sender_id,
                data: payload.native,
                room_id: this.state.room_id,
                category: "Peoples",
                count: 1,
                created_at: created
            }
            await axios.post("https://dm.zuri.chat/api/v1/rooms/6146cb29845b436ea04d1029/messages/6146d432845b436ea04d103b/reactions", newEmoji)
            .catch(error => {
                console.log(error)
            })
        },
        async setEmojis({state},payload) {
            const emoji = payload;
            emoji.count = 1
            emoji.room_id = state.room_id
            await axios.post("https://dm.zuri.chat/api/v1/rooms/6146cb29845b436ea04d1029/messages/6146d432845b436ea04d103b/reactions", emoji)
            .then(result => {
                console.log(result.data)
            }).catch(error => {
                console.log(error)
            })
        },
        async fetchEmojis({ commit }) {
            // GET IS WORKING
            try {
                await apiServices.getEmojis("6146cb29845b436ea04d1029", this.state.message_id)
                    .then(result => {
                        const emojis = result.data.data.reactions;
                        const emojiCount = [...emojis.reduce((r, e) => {
                            let k = `${e.data}|${e.name}`;
                            if (!r.has(k)) r.set(k, { ...e, count: 1 })
                            else r.get(k).count++
                            return r;
                        }, new Map).values()];
                        commit('setEmojiSet', emojiCount);
                        commit('addEmojis', result.data.data.reactions);
                    })
            } catch (error) {
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
