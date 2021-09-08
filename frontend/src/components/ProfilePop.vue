<template>
    <transition name="fade" appear>
        <div class="modal-overlay">
            <div class="pop">
                <div class="head">
                    <div class="profile_layout">
                        <div class="profile">
                            <img src="https://picsum.photos/200/300" alt="profile_pic" class="img">
                            <div class="profile_text">
                                <h1>Mama Gee 🦊 ⭐️</h1> 
                                <p>Frontend Design Mentor</p>
                                <p>She/Her</p>
                            </div>
                        </div>
                        <b-icon icon="x" scale="2" @click="$emit('close')" class="close"></b-icon>
                    </div>
                    <b-button class="mt-4 btn_mute"><i class="far fa-bell-slash mute"></i>Mute</b-button>
                    <div class="switch">
                        <div class="abt">About</div>
                        <div class="int">Integrations</div>
                    </div>
                </div>
                <div class="body">
                    <div class="card_1">
                        <div class="mb"><b-icon icon="clock" scale="1.3" class="card_icon"></b-icon> <span class="text_gray">3:15AM Local Time</span> </div>
                        <div class="mb"><b-icon icon="telephone" scale="1.3" class="card_icon"></b-icon><span class="text_blue">+23701877832</span> </div>
                        <div class="mb"><b-icon icon="envelope" scale="1.3" class="card_icon"></b-icon><span class="text_blue">mamagee@gmail.com</span> </div>
                        <p class="view_profile text_blue"> View Profile</p>
                    </div>
                    <div class="card_2">
                        <h1>Files</h1>
                        <p>There aren’t any files to see here. But there could be - drag and drop any file to the message panel to add it to this conversation</p>
                    </div>
                </div>
            </div>
        </div>
    </transition>
</template>

<script>
export default {
    emits:['close']
}
</script>

<style scoped>
    .modal-overlay {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        z-index: 2;
        background-color: rgba(0, 0, 0, 0.45);
    }
    .pop{
        z-index: 10;
        background: #F6F6F6;
        width: 680px;
        height: 100%;
        margin: 4% auto;
        /* padding: 24px 33px; */
        border-radius: 8px;
    }
    .head{
        background: white;
        padding: 24px 33px 0px;
    }
    .profile{
        display: flex;
    }
    .img{
        width: 85px;
        height: 94px;
        border-radius: 6px;
        margin-right: 19px;
    }
    .profile_layout {
        display: flex;
        justify-content: space-between;
    }
    .profile_text h1{
        font-size: 25px;
        font-weight: 700;
        margin-bottom: 6px;
    }
    .profile_text p{
        font-size: 15px;
        margin-bottom: 3px;
        color: #3A3A3A;
    }
    .close{
        cursor: pointer;
    }
    .btn_mute,
    .btn_mute:hover{
        border: 1px solid #979797;
        background: transparent;
        border-radius: 6px;
        color: #3A3A3A;
        font-size: 12px;
        font-weight: 700;
        padding: 9px 20px 9px 15px;
    }
    .mute{
        margin-right: 9px;
    }
    .switch{
        display: flex;
        margin-top:21px ;
        font-size: 15px;
    }
    .abt{
        margin-right: 32px;
        border-bottom:1px solid #00B87C ;
        padding-bottom: 11px;
    }
    .body{
        padding: 20px 35px 0px;
    }
    .card_1,
    .card_2{
        background: #FFFFFF;
        border-radius: 8px;
        font-size: 15px;
    }
    .card_1{
        padding: 26px 26px 21px;
        margin-bottom: 21px;
    }
    .card_icon{
        margin-right: 12px;
    }
    .mb{
        margin-bottom: 20px;
    }
    .text_gray{
        color: #3A3A3A;
        cursor: pointer;
    }
    .text_blue{
        color: #1A61DB;
        cursor: pointer;
    }
    .view_profile{
        font-weight: 700;
        margin-bottom: 0;
    }
    .card_2{
        padding: 20px 20px;
    }
    .card_2 h1{
        font-size: 15px;
        font-weight: 700;
    }
</style>