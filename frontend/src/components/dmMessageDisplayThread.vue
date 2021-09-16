<template>
    <div class="message-thread px-3 py-2">
        <div
            @mouseover="hover = true"
            @mouseleave="hover = false"
            class="msgBody position-relative"
        >
            <div class="conversation-threads d-flex flex-row">
                <div class="userProfile-avatar" @click="show_popup_profile(p_state = !p_state)">
                    <img src="https://picsum.photos/200/300" alt="{}" />
                </div>
                <div class="usertext-messages">
                    <h5 class="pb-2">
                        <span class="userName" @click="show_popup_profile(p_state = !p_state)">MamaGee</span>
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
                    <div v-if="emojis" class="reactions d-flex">
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
            p_state:false
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
        show_popup_profile(p_state){
            bus.$emit('togleProfilePopUp', p_state)
        }
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
    cursor:pointer;
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
.usertext-messages .userName{
    cursor:pointer
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
</style>
