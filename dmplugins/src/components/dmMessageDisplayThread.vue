<template>
    <div class="message-thread px-3 py-2">
        <div
            @mouseover="hover = true"
            @mouseleave="hover = false"
            class="msgBody position-relative"
        >
            <div class="conversation-threads d-flex flex-row">
                <div
                    class="userProfile-avatar"
                    @click="show_popup_profile((p_state = !p_state))"
                >
                    <img src="https://picsum.photos/200/300" alt="{}" />
                </div>
                <div class="usertext-messages">
                    <h5 class="pb-2">
                        <span
                            class="userName"
                            @click="show_popup_profile((p_state = !p_state))"
                            >MamaGee</span
                        >
                        <span class="msgTime">5.55pm</span>
                    </h5>
                    <div class="text-container">
                        <messageHoverShow v-if="hover" />
                        <p class="text">
                            Lorem ipsum dolor sit, amet consectetur adipisicing
                            elit. Eum mollitia aspernatur laboriosam cum
                            officiis commodi deleniti odit rerum ratione
                            consectetur. Lorem ipsum dolor sit amet, consectetur
                            adipiscing elit. Tincidunt adipiscing et, tortor,
                            fusce quis tellus, enim. A, posuere mi auctor odio
                            tincidunt magnis.
                        </p>
                    </div>
                    <div v-if="emojis.length > 0" class="reactions d-flex">
                        <div
                            v-for="(value, name, index) in emojiSet"
                            :key="index"
                        >
                            <div
                                class="thread-reactions"
                                @click="postSelect(name)"
                            >
                                {{ name }}
                                <div class="reaction-count">{{ value }}</div>
                            </div>
                        </div>
                        <div class="add-reactions" @click="addEmoji">
                            <svg
                                width="24"
                                height="24"
                                viewBox="0 0 11 12"
                                fill="none"
                                xmlns="http://www.w3.org/2000/svg"
                            >
                                <path
                                    d="M9.03907 5.24972C9.03901 4.3516 8.77021 3.47404 8.26725 2.72996C7.7643 1.98588 7.0502 1.40932 6.21683 1.07447C5.38347 0.739614 4.46898 0.661788 3.59101 0.851002C2.71305 1.04022 1.91179 1.48781 1.29033 2.1362C0.668874 2.78459 0.255649 3.60411 0.103827 4.4893C-0.0479946 5.3745 0.068533 6.28487 0.438416 7.10329C0.8083 7.92171 1.41462 8.61072 2.17935 9.08168C2.94409 9.55264 3.83225 9.78399 4.72957 9.74597C4.64452 9.50453 4.5874 9.25415 4.55932 8.99972H4.53907C3.79739 8.99972 3.07236 8.77978 2.45568 8.36773C1.83899 7.95567 1.35835 7.37 1.07452 6.68478C0.790689 5.99956 0.716426 5.24556 0.861121 4.51813C1.00582 3.7907 1.36297 3.12251 1.88741 2.59807C2.41186 2.07362 3.08005 1.71647 3.80748 1.57177C4.53491 1.42708 5.28891 1.50134 5.97413 1.78517C6.65935 2.069 7.24502 2.54964 7.65708 3.16633C8.06913 3.78301 8.28907 4.50804 8.28907 5.24972V5.26997C8.54782 5.29922 8.79757 5.35697 9.03532 5.44022C9.03757 5.37722 9.03907 5.31347 9.03907 5.24972Z"
                                    fill="#1D1C1D"
                                />
                                <path
                                    d="M4.62305 7.87273C4.68605 7.59673 4.78205 7.33348 4.90805 7.08823C4.58776 7.15307 4.25606 7.13283 3.94603 7.02953C3.63599 6.92623 3.35845 6.74348 3.14105 6.49948C3.07372 6.42965 2.98194 6.38862 2.885 6.38502C2.78806 6.38143 2.69349 6.41554 2.62117 6.48019C2.54884 6.54485 2.50439 6.63501 2.49714 6.73175C2.4899 6.82849 2.52042 6.92428 2.5823 6.99898C2.83767 7.28505 3.15272 7.51157 3.50521 7.66254C3.85771 7.81352 4.23905 7.88527 4.6223 7.87273H4.62305Z"
                                    fill="#1D1C1D"
                                />
                                <path
                                    d="M3.78906 4.5C3.78906 4.64918 3.7298 4.79226 3.62431 4.89775C3.51882 5.00324 3.37575 5.0625 3.22656 5.0625C3.07738 5.0625 2.9343 5.00324 2.82881 4.89775C2.72333 4.79226 2.66406 4.64918 2.66406 4.5C2.66406 4.35082 2.72333 4.20774 2.82881 4.10225C2.9343 3.99676 3.07738 3.9375 3.22656 3.9375C3.37575 3.9375 3.51882 3.99676 3.62431 4.10225C3.7298 4.20774 3.78906 4.35082 3.78906 4.5Z"
                                    fill="#1D1C1D"
                                />
                                <path
                                    d="M5.85156 5.0625C6.00075 5.0625 6.14382 5.00324 6.24931 4.89775C6.3548 4.79226 6.41406 4.64918 6.41406 4.5C6.41406 4.35082 6.3548 4.20774 6.24931 4.10225C6.14382 3.99676 6.00075 3.9375 5.85156 3.9375C5.70238 3.9375 5.5593 3.99676 5.45382 4.10225C5.34833 4.20774 5.28906 4.35082 5.28906 4.5C5.28906 4.64918 5.34833 4.79226 5.45382 4.89775C5.5593 5.00324 5.70238 5.0625 5.85156 5.0625Z"
                                    fill="#1D1C1D"
                                />
                                <path
                                    d="M10.5391 8.625C10.5391 9.32119 10.2625 9.98887 9.77022 10.4812C9.27793 10.9734 8.61026 11.25 7.91406 11.25C7.21787 11.25 6.55019 10.9734 6.05791 10.4812C5.56562 9.98887 5.28906 9.32119 5.28906 8.625C5.28906 7.92881 5.56562 7.26113 6.05791 6.76884C6.55019 6.27656 7.21787 6 7.91406 6C8.61026 6 9.27793 6.27656 9.77022 6.76884C10.2625 7.26113 10.5391 7.92881 10.5391 8.625ZM8.28906 7.125C8.28906 7.02554 8.24955 6.93016 8.17923 6.85983C8.1089 6.78951 8.01352 6.75 7.91406 6.75C7.81461 6.75 7.71922 6.78951 7.6489 6.85983C7.57857 6.93016 7.53906 7.02554 7.53906 7.125V8.25H6.41406C6.31461 8.25 6.21922 8.28951 6.1489 8.35983C6.07857 8.43016 6.03906 8.52554 6.03906 8.625C6.03906 8.72446 6.07857 8.81984 6.1489 8.89017C6.21922 8.96049 6.31461 9 6.41406 9H7.53906V10.125C7.53906 10.2245 7.57857 10.3198 7.6489 10.3902C7.71922 10.4605 7.81461 10.5 7.91406 10.5C8.01352 10.5 8.1089 10.4605 8.17923 10.3902C8.24955 10.3198 8.28906 10.2245 8.28906 10.125V9H9.41406C9.51352 9 9.6089 8.96049 9.67923 8.89017C9.74955 8.81984 9.78906 8.72446 9.78906 8.625C9.78906 8.52554 9.74955 8.43016 9.67923 8.35983C9.6089 8.28951 9.51352 8.25 9.41406 8.25H8.28906V7.125Z"
                                    fill="#1D1C1D"
                                />
                            </svg>
                        </div>
                    </div>
                    <EmojiComp :onSelectEmoji="onSelectEmoji" />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { bus } from '@/main.js';

import { mapActions, mapGetters, mapMutations } from 'vuex';
import messageHoverShow from '../components/common/dmThreadHoverState.vue';
import EmojiComp from '../components/common/dmEmojis.vue';
export default {
    name: 'DmMesssageThread',
    components: {
        messageHoverShow,
        EmojiComp,
    },
    data() {
        return {
            hover: false,
            p_state: false,
        };
    },
    methods: {
        ...mapActions(['setEmojis']),
        ...mapMutations(['setPickEmoji']),
        onSelectEmoji(emoji) {
            this.setPickEmoji(false);
            this.setEmojis(emoji.data);
        },
        postSelect(name) {
            this.setEmojis(name);
        },
        show_popup_profile(p_state) {
            bus.$emit('togleProfilePopUp', p_state);
        },
        addEmoji() {
            this.setPickEmoji(true);
        },
    },
    computed: {
        ...mapGetters(['emojis', 'emojiSet']),
    },
};
</script>

<style scoped>
:root {
    --main-green: #00b87b;
}
.message-thread {
    position: relative !important;
    background: #fff;
}
.conversation-threads {
    margin-bottom: 32px;
}

.userProfile-avatar {
    cursor: pointer;
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
.usertext-messages .userName {
    cursor: pointer;
}
.text-container {
    position: relative;
}

.msgBody:hover {
    background: var(--bg-color-footer);
}

.thread-reactions,
.add-reactions {
    background: rgba(29, 28, 29, 0.06);
    border-radius: 25px;
    padding: 1px 10px;
    position: relative;
    cursor: pointer;
}

.add-reactions {
    margin-left: 5px;
}

.add-reactions img {
    width: 20px;
    height: 20px;
}

.thread-reactions {
    display: inline-flex;
    justify-content: space-evenly;
    margin-right: 5px;
}

.reaction-count {
    font-size: 12px;
    margin-top: 2px;
    padding-left: 2px;
}
</style>
