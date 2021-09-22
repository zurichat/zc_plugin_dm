<template>
    <div class=" userContainer  shadow  bg-white">
        <div class="overlay" v-if="userProfile.status == false">
            <div>
            <p>Loading.....</p>
            </div>
        </div>
        <b-img class="u_icon" :src="userData.profileImage"></b-img>
        <div class="px-3">
            <div style="font-size:22px">
                <b>{{ userProfile.display_name }}</b>
                <!-- {{userProfile}} -->
            </div>
            <div style="font-size:12px">
                {{ userData.profession }}<br />
                {{ userProfile.pronouns }}
                <div class="mt-4" style="cursor:pointer; color:blue" @click="showFullProfile(true)">
                    View Full Profile
                </div>
            </div>
            <div class="text-muted">
                <small style="font-size:;margin-top:32px">Status</small><br />
                <i class="fa fas fa-cat"></i>

                <div style="margin:26.18px 0 27px 0;  font-size:12px">
                    <div class="text-muted"></div>
                    <div>{{ userProfile.localTime }}</div>
                </div>
            </div>
            <div class="d-flex justify-content-between mb-3 popup_footer">
                <b-button size="sm" variant="outline-secondary" class="lh-1"
                    >Message</b-button
                >
                <b-button size="sm" variant="outline-secondary" class="lh-1"
                    >Mute</b-button
                >
            </div>
        </div>
    </div>
</template>

<script>
import { bus } from '@/main.js';

export default {
    data() {
        return {
            toggle_popup: true,
            showLoading:false,
            userData: {
                displayName: 'Mama Gee',
                profession: 'Frontend Desing Mentor',
                gender: 'he/her',
                phoneNumber: '021345789',
                profileImage: 'https://picsum.photos/200/300',
            },
        };
    },
    methods: {
        showFullProfile(status){
            bus.$emit("showFullProfile", status)
            bus.$emit("togleProfilePopUp", !status);
        }
    },
    computed:{
        getTodayTime(){
            return new Date();
            // return this.today.getHours() + ":" + this.today.getMinutes();
        },
        userProfile(){
            return this.$store.state.userProfile
        }
        // METHOD TO GET THE DATA COMEING FROM dmMessageDisplayThread.vue
        // getUserProfileDetails(){

        // }
    },
    created() {
        // METHOD TO CLOSE THE COMPONENT IF USER CLICK OUTSIDE OF IT
        window.addEventListener('click', (e) => {
            if (!this.$el.contains(e.target)) {
                // window.close();
                // AN EVENT WOULD BE TRIGGERD HERE IF USER CLICK OUTSIDE THE DIV
                // I WANT THIS COMPONENT TO HIDE WHEN USER CLICK OUTSIDE
            }
        });
    },
};
</script>

<style scoped>
.overlay{
    position: absolute;
    height: 100%;
    width: 100%;
    background-color: rgba(18, 21, 22, 0.466);  /* 100% transparent */
    color:#fff;
    text-align: center;
    justify-content: center;
    display: flex;
    align-items: center;
    font-weight: bolder;
}
.popup_footer button {
    width: 117px;
    height: 32px;
}
.primaryColor {
    background-color: #00b87c;
}
.userContainer {
    position: absolute;
    z-index: 1;
    width: 280px;
    /* min-height: 632px; */
    /* height: 60vh; */
    top: 10%;
    font-family: 'Lato', sans-serif;
    left: 100.5px;
    /* right: 40%; */
}

.u_icon {
    width: 100%;
    height: 230px;
    margin: 0px 0px 16px 0px;
    object-fit: cover;
}
.btn-rounded {
    border-radius: 100%;
}

.profile_icons button {
    height: 65%;
}
</style>
