<template>
    <div class=" userContainer  shadow  bg-white">
        <b-img class="u_icon" :src="userData.profileImage"></b-img>
        <div class="px-3">
            <div style="font-size:22px">
                <b>{{ userData.displayName }}</b>
            </div>
            <div style="font-size:12px">
                {{ userData.profession }}<br />
                {{ userData.gender }}
                <div class="mt-4">
                    <a href="#" class="text-decoration-none"
                        >View Full Profile</a
                    >
                </div>
            </div>

            <div class="text-muted">
                <small style="font-size:;margin-top:32px">Status</small><br />
                <i class="fa fas fa-cat"></i>

                <div style="margin:26.18px 0 27px 0;  font-size:12px">
                    <div class="text-muted">Local Time</div>
                    <div>{{ userData.localTime }}</div>
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
            userData: {
                displayName: 'Mama Gee',
                profession: 'Frontend Desing Mentor',
                gender: 'he/her',
                localTime: '3:15PM',
                phoneNumber: '021345789',
                //  profileImage:require('@/assets/images/mamaGee.jpg')
                profileImage: 'https://picsum.photos/200/300',
            },
        };
    },
    methods: {},
    created() {
        window.addEventListener('click', (e) => {
            if (!this.$el.contains(e.target)) {
                window.close();
                // AN EVENT WOULD BE TRIGGERD HERE IF USER CLICK OUTSIDE THE DIV
                // I WANT THIS COMPONENT TO HIDE WHEN USER CLICK OUTSIDE
            }
        });
    },
};
</script>

<style scoped>
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
