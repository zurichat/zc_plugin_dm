<template>
    <div class="input-container px-3 pb-3">
        <div class="input-form-field">
            <b-form-textarea
                id="textarea-no-resize"
                placeholder="Send message to "
                rows="1"
                class="px-3 py-2"
                v-model="sendMsg"
                style="border: none; overflow-y: hidden; height: calc(0.5em + 0.25em + 1px);"
                no-resize
            ></b-form-textarea>
            <div
                class="emoji-htmlformat-group d-flex flex-row justify-space-between px-1"
            >
                <b-col class="html-format d-flex align-items-center">
                    <span class="lighting-icon btnf input-emoji-icons">
                        <b-icon icon="lightning" aria-hidden="true"></b-icon>
                    </span>
                    <div class="html-format-type d-flex align-items-center">
                        <span class="btnf input-emoji-icons">
                            <b-icon-type-bold></b-icon-type-bold>
                        </span>
                        <span class="btnf input-emoji-icons">
                            <b-icon-type-italic></b-icon-type-italic>
                        </span>
                        <span class="btnf input-emoji-icons">
                            <b-icon-link-45deg></b-icon-link-45deg>
                        </span>
                        <span class="btnf input-emoji-icons">
                            <b-icon-list-ul></b-icon-list-ul>
                        </span>
                    </div>
                </b-col>
                <div class="emoji-selector-send  d-flex align-items-center">
                    <span class="btnf input-emoji-icons">
                        <b-icon-at></b-icon-at>
                    </span>
                    <span class="btnf input-emoji-icons">
                        <b-icon-paperclip rotate="45"></b-icon-paperclip>
                    </span>
                    <span :class="this.sendMsg.length > 0 ? 'send' : 'notSend'">
                        <span class="btnf input-send">
                            <b-icon-cursor-fill
                                rotate="45"
                            ></b-icon-cursor-fill>
                        </span>
                        <span
                            :class="
                                this.sendMsg.length > 0
                                    ? 'divider'
                                    : 'notSendDivider'
                            "
                        ></span>
                        <!--added a click event to make request:deveeb-->
                        <span
                         class="btnf input-send-reminder"
                         @click="makeRequest">
                            <b-icon-chevron-down></b-icon-chevron-down>
                        </span>
                    </span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
// importing makeRequest action from vuex store:deveeb
import {mapActions} from 'vuex'

export default {
    name: 'inputContainer',
    data() {
        return {
            message: 'Hello',
            sendMsg: '',
        };
    },
    methods:{
        //calling makeRequest:deveeb
    ...mapActions(['makeRequest'])
  }
};
</script>

<style scoped>
.input-form-field {
    background: #fff;
    border: 1px solid #ebebeb;
    border-radius: 3px;
    flex: 1;
}

span.lighting-icon {
    border-right: 1px solid #ccc;
    padding: 0 6px;
}

.input-text-area {
    border: none;
    overflow-y: hidden;
    resize: none;
    line-height: 1.7;
    font-size: 15px;
    max-height: 180px;
}

.btnf.input-emoji-icons {
    margin: 0;
    font-size: 20px;
    cursor: pointer;
    user-select: none;
    outline: none;
    padding: 0 8px;
}

.btnf.input-emoji-icons:hover,
.btnf.input-emoji-icons:focus {
    color: #fff;
    background-color: rgb(234, 234, 234);
    border-radius: 4px;
}

span.btnf.input-send,
span.btnf.input-send-reminder {
    padding: 0 8px;
    cursor: pointer;
    user-select: none;
    outline: none;
}

.send {
    background-color: var(--color-hover-send);
    padding: 8px;
    margin-left: 4px;
    color: white;
    border-radius: 4px;
}

.notSend {
    background-color: transparent;
    padding: 11px 8px;
    margin-left: 4px;
    color: #ccc;
    border-radius: 4px;
}

.divider {
    padding: 0px 4px;
    border-right: 1px solid white;
}

.notSendDivider {
    padding: 0px 4px;
    border-right: 1px solid grey;
}
</style>
