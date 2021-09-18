<template>
    <div class="hover-state-message">
        <div
            class="thread-message-hover-state d-flex flex-row justify-content-between align-items-center"
        >
            <div
                class="thread-message-emojis py-1 px-2 thread-message-hover"
                data-toggle="tooltip"
                data-placement="top"
                tabindex="0"
                title="Add a reaction"
                variant="danger"
                v-b-tooltip.hover.focus
                @click="pickEmoji"
            >
                <b-icon icon="emoji-smile" font-scale="1.3" />
            </div>
            <div
                class="reply-thread-message py-1 px-2 thread-message-hover"
                data-toggle="tooltip"
                data-placement="top"
                tabindex="0"
                title="Reply in thread"
                v-b-tooltip.hover.focus
                @click="showReply"
            >
                <b-icon icon="chat-text" font-scale="1.3" />
            </div>
            <div
                class="share-thread-message py-1  px-2 thread-message-hover"
                data-toggle="tooltip"
                data-placement="top"
                tabindex="0"
                title="Share message..."
                v-b-tooltip.hover.focus
            >
                <b-icon icon="reply" font-scale="1.3" />
            </div>
            <div
                class="bookmark-thread-message py-1 px-2 thread-message-hover"
                data-toggle="tooltip"
                data-placement="top"
                tabindex="0"
                title="Add to saved items"
                v-b-tooltip.hover.focus
            >
                <b-icon icon="bookmark" font-scale="1.3" />
            </div>
            <div
                class="more-message-action py-1 px-2 thread-message-hover"
                data-toggle="tooltip"
                data-placement="topleft"
                title="More actions"
                v-b-tooltip.hover.focus
            >
                <b-iconstack font-scale="1.3">
                    <b-icon stacked icon="dot" shift-v="5" />
                    <b-icon stacked icon="dot" />
                    <b-icon stacked icon="dot" shift-v="-5" />
                </b-iconstack>
            </div>
        </div>
    </div>
</template>

<script>
import { mapMutations } from 'vuex';

export default {
    name: 'dmThreadHoverState',
    data() {
        return {};
    },
    methods: {
        ...mapMutations(['setPickEmoji', 'setShowReply']),
        pickEmoji() {
            this.setPickEmoji(true);
        },
        showReply() {
            this.setShowReply(true);
        },
    },
};
</script>

<style scoped>
.hover-state-message {
    position: absolute;
    right: 0;
    top: -20%;
}

.thread-message-hover-state {
    background: #fff;
    border: 1px solid #ccc;
    width: 190px;
    height: auto;
    padding: 3px;
    border-radius: 8px;
}

.thread-message-hover-state + .tooltip > .tooltip-inner {
    padding: 1.5rem;
    background-color: white;
    color: #261e1c;
    font-size: 2rem;
    text-align: center;
}

.thread-message-hover:hover {
    cursor: pointer;
    outline: none;
    user-select: none;
    background: #f6f6f6;
    border-radius: 4px;
}
</style>
