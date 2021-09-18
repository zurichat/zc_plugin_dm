<template>
    <div class="home position-relative d-flex ">
        <div
            class="direct-message-contents d-flex flex-column position-relative"
        >
            <div class="profile-pop-up" v-if="toggleProfilePopUp">
                <PopupProfile />
            </div>
            <div class="direct-message-header">
                <DmProfileHeader />
            </div>
            <div
                class="direct-message-body-contents d-flex flex-column position-relative"
            >
                <div class="direct-message-allmessages-body position-relative">
                    <DmSingleMessageBox />
                </div>
                <div class="direct-message-input-footer">
                    <DmInputxtf />
                </div>
            </div>
        </div>
        <div class="profileContainer">
            <!-- <ProfileContainer /> -->
        </div>
    </div>
</template>

<script>
import { bus } from '../main.js';
// @ is an alias to /src
import DmProfileHeader from '@/components/dmProfileHeader.vue';
import Bookmark from '@/components/bookmarks.vue';
import DmInputxtf from '@/components/dmInputTextField.vue';
import DmSingleMessageBox from '@/components/dmSingleMessageBox.vue';
import PopupProfile from '@/components/common/popupProfile';

export default {
    name: 'Home',
    components: {
        DmProfileHeader,
        Bookmark,
        DmInputxtf,
        DmSingleMessageBox,
        PopupProfile,
    },
    data() {
        return {
            toggleProfilePopUp: false,
        };
    },
    created() {
        bus.$on('togleProfilePopUp', (p_state) => {
            this.toggleProfilePopUp = p_state;
        });
    },
};
</script>

<style scoped>
div.home {
    width: 100%;
    background-color: #f9f9f9;
}

div.home .direct-message-contents {
    min-width: 0;
    min-height: 0;
    background-color: #f9f9f9;
}

.direct-message-body-contents {
    flex: 1;
    min-height: 0;
}

.direct-message-allmessages-body {
    flex: 1;
    min-height: 0;
}

.direct-message-input-footer {
    display: flex;
    flex-flow: column;
    justify-content: flex-end;
}
</style>
