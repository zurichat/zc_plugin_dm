<template>
    <div class="row align-items-end message-box">
        <div class="d-flex flex-column col-auto">
            <div class="d-flex align-item-center flex-row py-4 px-3">
                <div class="col-auto align-self-center link-btn ">
                    <button class="btn-outline-disabled btn-dm-chat">
                        <b-icon-chat-dots scale="1.5"></b-icon-chat-dots>
                    </button>
                </div>
                <div class="px-3 chat-description">
                    <h4 class="m-0">
                        This conversation is just between two of you
                    </h4>
                    <p class="m-0">
                        Here you can send messages and share files with
                        <span class="username-id">@ o4codes</span>
                    </p>
                </div>
            </div>

            <DmMessageDisplayThread />
        </div>
    </div>
</template>

<script>
// @alias
import DmMessageDisplayThread from './dmMessageDisplayThread.vue';
export default {
    name: 'messagebox',
    components: {
        DmMessageDisplayThread,
    },
    data() {
        return {};
    },
    computed: {},
    methods: {},
};
</script>

<style scoped>
.message-box {
    height: 75vh;
    overflow-y: scroll;
    display: flex;
    flex-flow: row wrap;
}

.message-stack {
    width: 100%;
    border: 1px solid gray;
}

.welcome-text {
    width: 100%;
    border: 1px solid gray;
}

/*  */

.btn-dm-chat {
    width: 45px;
    height: 45px;
    background-color: #fff;
    box-shadow: 0 3px 6px rgba(97, 96, 97, 0.03);
    padding: 0;
    border: none;
    user-select: none;
    cursor: pointer;
    outline: none;
}

.bi-chat-dots.b-icon.bi {
    background: rgba(0, 0, 0, 0.15);
}

.chat-description h4 {
    font-size: 15px;
    font-weight: 700;
    line-height: 1.75;
}

.chat-description p {
    font-size: 13px;
    font-weight: normal;
    line-height: 1.5;
}

.username-id {
    color: var(--color-hover-send);
    cursor: pointer;
    user-select: none;
    outline: none;
    padding-left: 5px;
}
</style>
