<template>
  <div>
    <div class="message-thread px-3 py-2">
        <!--THIS IS THE CHAT BOX THINGY AT THE TOP-->
        <div class="d-flex flex-column col-auto">
            <div class="d-flex align-item-center flex-row py-4 px-3">
                <div class="col-auto align-self-center link-btn ">
                    <button class="btn-outline-disabled btn-dm-chat">
                        <b-icon-chat-dots scale="1.5"></b-icon-chat-dots>
                    </button>
                </div>
                <div class="px-3 chat-description">
                    <h4 class="m-0">
                        This conversation is just between two of you
                    </h4>
                    <p class="m-0">
                        Here you can send messages and share files with
                        <span class="username-id">@ o4codes</span>
                    </p>
                </div>
            </div>
        </div>
        <!--MESSAGES START FROM HERE-->
        <div v-for="message in showMessages" :key="message._id">
            <div
            @mouseover="hover = true"
            @mouseleave="hover = false"
            class="msgBody position-relative"
           >
            <div class="conversation-threads d-flex flex-row">
                <div class="userProfile-avatar">
                    <img src="https://picsum.photos/200/300" alt="{}" />
                </div>
                <div class="usertext-messages">
                    <h5 class="pb-2">
                        <span class="userName">MamaGee</span>
                        <span class="msgTime">{{ getHumanDate(message.created_at)}}</span>
                    </h5>
                    <div class="text-container">
                         <messageHoverShow v-if="hover" />
                        <p class="text">
                            {{ message.message}}
                        </p>
                    </div>
                </div>
            </div>  
           </div>
        </div>
    </div>
    <div class="row align-items-end message-box">
        <!--FOR SOME REASON WHEN I DELETE THIS IT MESSES UP THE CODE SO DON'T TAKE IT OUT UNLESS YOU FIND A SOLUTION-->
    </div>
    <DmInputTextField />
  </div>

</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import messageHoverShow from '../components/common/dmThreadHoverState.vue';
import DmInputTextField from '../components/dmInputTextField.vue'
import moment from 'moment'
export default {
    name: 'DmMesssageThread',
    components: {
        messageHoverShow,
        DmInputTextField

    },
    data() {
        return {
            hover: false,
        };
        
    },
    methods: { 
        ...mapActions(["fetchMessages"]),
        //TIME STAMP FUNCTION
        getHumanDate : function (created_at) {
                return moment(created_at, 'LT').format('LT');
        }
    },
    computed: {
        ...mapGetters(["showMessages"]),
    },
    created(){
      this.fetchMessages();
    }
};
</script>

<style scoped>
:root {
    --main-green: #00b87b;
}
.message-thread {
    position: relative !important;
    background: #fff;
    top: 420px;
}
.conversation-threads {
    margin-bottom: 32px;
}

.userProfile-avatar {
    padding-right: 16px;
}

.userProfile-avatar img {
    vertical-align: middle;
    width: 36px;
    height: 36px;
    border-radius: 4px;
}

.usertext-messages {
    font-size: 15px;
    line-height: 1.8;
}

.usertext-messages h5 {
    margin-bottom: 0;
    font-size: 16px;
    font-weight: 600;
}

.usertext-messages span.msgTime {
    padding-left: 8px;
    font-size: 12px;
    color: #999999;
    font-weight: 400;
}

.usertext-messages p {
    margin-bottom: 0;
}

.text-container {
    position: relative;
}

.msgBody:hover {
    background: var(--bg-color-footer);
}

.thread-reactions {
    border: 1px solid #00b87b !important;
    border-radius: 25px;
    padding: 1px 8px;
    position: relative;
    display: inline-block;
    margin-right: 5px;
    cursor: pointer;
}
.reaction-count {
    position: absolute;
    bottom: 0;
    right: 4px;
    font-size: 10px;
    font-weight: 700;
}

.message-box {
    height: 70vh;
    overflow-y: scroll;
    display: flex;
    flex-flow: row wrap;
}

.message-stack {
    width: 100%;
    border: 1px solid gray;
}

.welcome-text {
    width: 100%;
    border: 1px solid gray;
}

/*  */

.btn-dm-chat {
    width: 45px;
    height: 45px;
    background-color: #fff;
    box-shadow: 0 3px 6px rgba(97, 96, 97, 0.03);
    padding: 0;
    border: none;
    user-select: none;
    cursor: pointer;
    outline: none;
}

.bi-chat-dots.b-icon.bi {
    background: rgba(0, 0, 0, 0.15);
}

.chat-description h4 {
    font-size: 15px;
    font-weight: 700;
    line-height: 1.75;
}

.chat-description p {
    font-size: 13px;
    font-weight: normal;
    line-height: 1.5;
}

.username-id {
    color: var(--color-hover-send);
    cursor: pointer;
    user-select: none;
    outline: none;
    padding-left: 5px;
}
</style>