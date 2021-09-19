<template>
    <div class="about">
        <div
            class="thread-message-hover-state d-flex flex-row justify-content-between"
        >
            <div class="thread-message-emojis">
                <b-icon icon="emoji-smile" />
            </div>
            <div class="reply-thread-message">
                <b-icon icon="chat-text" />
            </div>
            <div class="share-thread-message">
                <b-icon icon="share" />
            </div>
            <div class="bookmark-thread-message">
                <b-icon icon="bookmark" />
            </div>
            <div class="more-message-action">
                <b-iconstack>
                    <b-icon stacked icon="dot" shift-h="3" shift-v="3" />
                    <b-icon stacked icon="dot" shift-h="3" shift-v="3" />
                    <b-icon stacked icon="dot" shift-h="3" shift-v="3" />
                </b-iconstack>
            </div>
        </div>
    </div>
</template>

<script>
export default {};
</script>

<style scoped>
.about {
    background: chartreuse;
}

.thread-message-hover-state {
    background: #fff;
    border: 1px solid #ccc;
    width: 200px;
    height: auto;
    padding: 1.5px;
}

.thread-message-emojis {
    background: blueviolet;
}

.reply-thread-message {
    background: limegreen;
}
</style>
