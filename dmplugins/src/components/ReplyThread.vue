<template>
  <div class="reply-thread">
      <header class="reply-thread-header">
          <div>
                <p> Thread </p>
                <span>{{ displayName }}</span>
          </div>
          <i class="fas fa-times"></i>
      </header>

      <div class="reply-thread-headerSec">

      </div>

        <div class="reply-thread-messageBody">

            <div class="reply-thread-msgDetails reply-thread-receivedMsgContainer">
                <div class="reply-thread-msgImg reply-thread-receivedMsgImg">
                    <img :src="userTwoImg" alt="User Two Image">
                </div>
                <div class=" reply-thread-msgText reply-thread-receivedMsg">
                    <p><span class="userTwoUsername">{{ username }}</span> <span class="msgTime">6.05pm</span></p>
                    <p class="userTwoMessage">{{ replyThreadClickedMsg }}</p>
                </div>
            </div>

            <!-- Message Demarcation For Desktop Version -->
            <div class="msgDemarcation">
                <p class="newMsg"><span v-if="displayNewSentMsg" class="msgNumber">{{ msgLength }}</span> replies <span class="demarcation"></span></p> 
            </div>
            <!-- Ends Here -->

            <div v-if="displayNewSentMsg" v-for="msgDetails in replyThreadNewMsg" :key="msgDetails.index" class="reply-thread-recentMsgContainer">
                <div class="reply-thread-msgDetails reply-thread-recentMsgs">
                    <div class="reply-thread-msgImg reply-thread-imageContainer">
                        <img :src="msgDetails.img" alt="User Image">
                    </div>
                    <div class="reply-thread-msgText reply-thread-msgContainer">
                        <p><span class="userName">{{ msgDetails.username }}</span> <span class="msgTime">{{ msgDetails.msgTime }}</span></p>
                        <p class="text">{{ msgDetails.newMsg }}</p>
                    </div>
                </div>
            </div>
        </div>

      <div class="reply-thread-inputSection">
          
          <textarea ref="userMsg" placeholder="Send a message" name="userMessage" cols="30" rows="10"></textarea>

          <div class="reply-thread-icons">
              <div class="reply-thread-iconGroups">
                    <img src="../assets/zap.png" alt="Zap">
                    <img src="../assets/Line 7.png" alt="">
                    <img src="../assets/bold.png" alt="Bold">
                    <img src="../assets/italics.png" alt="Italics">
                    <img src="../assets/underline.png" alt="Underline">
              </div>
              <div class="reply-thread-iconGroups">
                    <img src="../assets/emoji.png" alt="Emoji">
                    <img src="../assets/paperclip.png" alt="Paper Clip">
                    <img @click="getMessage" src="../assets/send.png" alt="Send">
                    <img src="../assets/Line 7.png" alt="">
                    <img src="../assets/arrow-down.png" alt="Arrow Down">
              </div>
          </div>
        </div>
        <div class="reply-thread-addOpt">
            <input type="checkbox" >
            <p>Also send as direct message</p>
        </div>
    </div>
</template>

<script>
// import Centrifuge from 'centrifuge'

export default {
    name: 'ReplyThread',
    data () {
        return {
            displayNewSentMsg: false,
            sentMessages: '',
            userTwoImg: '',
            replyThreadUsername: '',
            msgLength: 0,
            replyThreadClickedMsg: '',
            displayName: 'Sandra Bernard',
            username: '',
            msgTime: '',
            newSentMessage: ''
        }
    },
    computed: {
        replyThreadNewMsg () {
            return this.$store.state.replyThreadMsgs.replyThreadNewMsg
        }
    },
    methods: {
        // Function to get the message sent by the user
        getMessage () {
            // get the message in the input box once the user clicks send
            this.newSentMessage = this.$refs.userMsg.value

            // Pushed all the user info including the message to vuex to create a store
            // This will be sent to the database throuh the endpoint if needed
            this.$store.state.replyThreadMsgs.replyThreadNewMsg.push({
                newMsg: this.newSentMessage,
                img: this.$store.state.replyThreadMsgs.userImg,
                // username here is the sender's user name, this is hard coded here
                // will be changed soon to the real username
                username: this.displayName,
                msgTime: this.getTime()
            })
            this.sendMessage()
            this.newMsgLength()
        },
        // Function to get the lenght of new messages
        newMsgLength () {
            this.msgLength = this.$store.state.replyThreadMsgs.replyThreadNewMsg.length
        },
        // Function to send message throughnthe endpoint
        sendMessage () {
            // sending the message through the endpoint
            fetch('https://dm.zuri.chat/api/v1/rooms/6146d126845b436ea04d102e/messages/6146ea68845b436ea04d107d/thread', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    "sender_id": '6146ce37845b436ea04d102d',
                    "message": this.newSentMessage
                })
            })
            .then((res) => {
                // Check if the message has been sent successfully
                if (res.statusText == 'Created') {
                    this.displayNewSentMsg = true
                    this.$refs.userMsg.value = ''
                }
                else {
                    this.displayNewSentMsg = false
                }
            })
            .catch(err => {
                console.log(err)
            })
        },
        //  Funtion to get the time the message was sent and display it
        getTime () {
            let today = new Date()
            let time = ''
            return time = today.getHours() + ":" + today.getMinutes()
        }
    },
    mounted () {
        console.log('working')
        // get the clicked message, the user image, username, and msg time
        // this will be displayed in the reply in thread window
        this.replyThreadClickedMsg = this.$store.state.replyThreadMsgs.clickedMsg
        this.userTwoImg = this.$store.state.replyThreadMsgs.userImg
        this.replyThreadUsername = this.$store.state.replyThreadMsgs.username
        this.username = this.$store.state.replyThreadMsgs.username
    }
}
</script>

<style scoped>
    .reply-thread {
        background-color: #fff;
        text-align: left;
        font-family: 'Lato';
        width: 400px;
        position: absolute;
        top: 0px;
        right: 0px;
        padding-bottom: 0px;
        box-sizing: border-box;
        height: 100vh;
        overflow: hidden;
    }
    .reply-thread-header {
        height: 42px;
        padding: 0px 30px 0px 30px;
        color: #fff;
        background-color: var(--bg-color-header);
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .reply-thread-header div {
        height: 40px;
        padding: 0px;
        padding-top: 5px;
    }
    .reply-thread-header div * {
        display: inline-block;
    }
    .reply-thread-header div p {
        font-size: 20px;
        font-weight: 600;
    }
    .reply-thread-header div span {
        font-size: 15px;
        margin: 0px 15px;
    }
    .reply-thread-header .fa-times {
        font-size: 20px;
        cursor: pointer;
    }
    .reply-thread-headerSec {
        height: 35px;
        background-color: var(--bg-color-footer);
    }

/* Clicked Message Displayed in the Thread */ 
    .reply-thread-msgDetails {
        padding: 0px 15px;
        margin: 0px 0px 15px 0px;
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
    }
    .reply-thread-msgImg {
        display: inline-block;
        width: 40px;
        height: 40px;
        border-radius: 3px;
        overflow: hidden;
    }
    .reply-thread-msgImg img {
        width: 100%;
    }
    .reply-thread-msgText {
        width: 83%;
    }
    .reply-thread-msgText p {
        margin: 0px 0px 5px 0px;
    }
    .reply-thread-msgText .userTwoUsername,
    .reply-thread-msgText .userName 
    {
        font-size: 16px;
        font-weight: 600;
        margin-right: 10px;
    }
    .reply-thread-msgText .msgTime {
        font-size: 12px;
        color: #999898;
    }
/* Ends Here */

/* Recent Messages */
    .reply-thread-recentMsg {
        padding: 0px 15px;
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
    }

/* Message Body Tag */
    .reply-thread-messageBody {
        padding-top: 20px;
        height: 67vh;
        overflow-y: scroll;
        overflow-x: hidden;
        background-color: #fff;
    }
    .currentMsg img {
        margin-right: 10px;
    }
    /* message demarcation */
    .msgDemarcation {
        margin: 10px 20px;
        position: relative;
    }
    .msgDemarcation .demarcation {
        position: absolute;
        border: thin solid #bdbdbd;
        width: calc(100% - 70px);
        top: 63%;
        transform: translateY(-50%);
        right: 0px;
        height: 2px;
    }
    /* message demarcation ends here */

/* Input Section Styles */
    .reply-thread-inputSection {
        border: thin solid #d5d4d4;
        padding: 0px 10px;
        margin: 0px 15px;
        background-color: #fff;
        position: relative;
        bottom: 0px;
        left: 0px;
    }
    .reply-thread-inputSection textarea {
        border: none;
        outline: none;
        width: 100%;
        height: 45px;
        font-size: 16px;
        font-family: 'Lato';
        opacity: 0.7;
        padding: 10px;
    }
    .reply-thread-icons {
        height: 30px;
        margin: 10px 0px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .reply-thread-iconGroups {
        display: flex;
        align-items: center;
    }
    .reply-thread-iconGroups img {
        cursor: pointer;
        margin: 0px 7px;
    }
/* Ends Here */

    .reply-thread-addOpt {
        margin-top: 5px;
        width: 100%;
        display: flex;
        align-items: flex-start;
    }
    .reply-thread-addOpt input {
        margin: 5px 10px 0px 15px;
    }
    @media screen and (max-width: 400px) {
        .reply-thread {
            width: 100vw;
            font-size: 14px !important;
        }
    }

</style>