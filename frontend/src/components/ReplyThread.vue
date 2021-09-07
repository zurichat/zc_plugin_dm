<template>
    <div class="messageThread">
        <header>
            <h1><i class="mobile fas fa-angle-left"></i> Thread</h1>
            <i class="fas fa-times"></i>
        </header>

        <div class="messageBody">
            <div class="messages currentMsg">
                <img src="../assets/Ellipse 21.png" alt="User Image" />
                <div class="userText">
                    <p>
                        <span class="userName">MamaGee</span>
                        <span class="msgTime">6.05pm</span>
                    </p>
                    <p class="text">
                        Lorem ipsum dolor sit, amet consectetur adipisicing
                        elit. Eum mollitia aspernatur laboriosam cum officiis
                        commodi deleniti odit rerum ratione consectetur.
                    </p>
                </div>

                <div class="userMsgOptions mobile">
                    <i class="far fa-grin"></i>
                    <div>
                        <p class="newMsg">3 replies</p>
                        <div class="msgOptions">
                            <i class="fas fa-long-arrow-alt-right"></i>
                            <i class="fas fa-ellipsis-v"></i>
                        </div>
                    </div>
                </div>
            </div>

            <!-- <div !v-if= new>
        p class="newMsg"><span class="msgNumber">3</span> replies</p> 
        </div> -->

            <div class="messages newMessages">
                <img src="../assets/Ellipse 24.png" alt="User Image" />
                <div class="userText">
                    <p>
                        <span class="userName">GeeGee</span>
                        <span class="msgTime">6.05pm</span>
                    </p>
                    <p class="text">
                        Lorem ipsum dolor sit, amet consectetur adipisicing
                        elit. Eum mollitia aspernatur laboriosam cum officiis
                        commodi deleniti odit rerum ratione consectetur.
                    </p>
                </div>
            </div>

            <div class="messages newMessages">
                <img src="../assets/Ellipse 21.png" alt="User Image" />
                <div class="userText">
                    <p>
                        <span class="userName">MamaGee</span>
                        <span class="msgTime">6.05pm</span>
                    </p>
                    <p class="text">
                        Lorem ipsum dolor sit, amet consectetur adipisicing
                        elit. Eum mollitia aspernatur laboriosam cum officiis
                        commodi deleniti odit rerum ratione consectetur.
                    </p>
                </div>
            </div>
        </div>

        <div class="inputSection">
            <textarea
                placeholder="Reply..."
                name="userMessage"
                cols="30"
                rows="10"
            ></textarea>
            <div class="textIcons">
                <div class="iconGroups">
                    <i class="fas fa-bolt"></i>
                    <img src="../assets/Line 7.png" alt="" />
                    <i class="fas fa-bold"></i>
                    <i class="fas fa-italic"></i>
                    <i class="fas fa-underline"></i>
                </div>
                <div class="iconGroups">
                    <i class="far fa-grin"></i>
                    <i class="fas fa-paperclip"></i>
                    <img src="../assets/Shape.png" alt="Send" />
                    <img src="../assets/Line 7.png" alt="" />
                    <i class="fas fa-angle-down"></i>
                </div>
            </div>
        </div>
        <input class="mobile" type="checkbox" name="" id="" />
        <p class="mobile">Also send as direct message</p>
    </div>
</template>

<script>
export default {
    data() {
        return {
            width: window.innerWidth,
        };
    },
    // mounted: function () {
    //     window.addEventListener('resize', function () {
    //         this.width = window.innerWidth
    //         console.log(this.width)
    //     })
    // }
};
</script>

<style scoped>
.messageThread {
    text-align: left;
    border: thin solid #e6e6e6;
    width: 400px;
    position: absolute;
    top: 10px;
    right: 15px;
    margin: 0px;
    font-size: 16px;
    padding: 0px;
    box-sizing: border-box;
}
header {
    height: 70px;
    padding: 0px 30px 0px 10px;
    color: #fff;
    background-color: #00bb7c;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
header .fa-times {
    font-size: 20px;
    cursor: pointer;
}

.messageBody {
    padding-top: 20px;
}
.messages {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    padding: 10px 20px;
}
.messages img {
    width: 200px;
    margin-right: 10px;
}
.userText {
    margin-left: 10px;
    text-align: left;
    line-height: 1.5;
}
.userText p {
    margin: 10px 0px;
}
.userName {
    font-weight: 900;
    font-size: 18px;
}
.msgTime {
    margin-left: 10px;
    font-weight: 100;
    font-size: 14px;
}

.inputSection {
    border: thin solid #d5d4d4;
    margin: 0px 15px;
    padding: 0px 10px;
}
.inputSection textarea {
    border: none;
    outline: none;
    width: 100%;
    height: 45px;
    font-size: 16px;
    opacity: 0.7;
}
.inputSection .textIcons {
    height: 30px;
    margin: 10px 0px;
}
.textIcons {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.iconGroups {
    display: flex;
    align-items: center;
}
.iconGroups * {
    cursor: pointer;
    font-size: 18px;
    margin: 0px 7px;
}

.messageThread input {
    margin: 0px 15px;
}
.messageThread > p {
    display: inline-block;
}

.mobile {
    display: none;
}

@media screen and (max-width: 600px) {
    .mobile {
        display: inline-block;
    }
    .messageThread {
        width: 100%;
        top: 0px;
        right: 0px;
        margin: 0px;
        font-size: 14px;
    }
    header {
        width: 100%;
        box-sizing: border-box;
        padding: 0px 30px 0px 10px;
        color: #fff;
        background-color: #00bb7c;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    header .fa-angle-left {
        margin-right: 10px;
        cursor: pointer;
    }
    .messages {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        padding: 10px 20px;
    }
    .currentMsg {
        flex-direction: column;
    }
    .currentMsg img {
        width: 50px;
    }
    .userMsgOptions {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: flex-start;
        width: 100%;
    }
    .userMsgOptions .fa-grin {
        font-size: 20px;
        cursor: pointer;
        padding: 3px 5px;
        border-radius: 5px;
        background-color: #dddcdc;
    }
    .userMsgOptions > div {
        display: flex;
        margin-top: 15px;
        border-top: thin solid #dddcdc;
        border-bottom: thin solid #dddcdc;
        align-items: center;
        width: 100%;
        justify-content: space-between;
    }
    .msgOptions {
        width: 100px;
        display: flex;
        align-items: center;
        justify-content: space-evenly;
    }
    .msgOptions .fa-long-arrow-alt-right,
    .msgOptions .fa-ellipsis-v {
        font-size: 20px;
        cursor: pointer;
    }
}
</style>
