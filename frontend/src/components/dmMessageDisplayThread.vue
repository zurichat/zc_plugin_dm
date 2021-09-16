<template>
    <div class="message-thread px-3 py-2">
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
                            <img src="@/assets/add-emoji.svg" alt="add-emoji" />
                        </div>
                    </div>
                    <EmojiComp :onSelectEmoji="onSelectEmoji" />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
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
