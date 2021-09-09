<template>
    <div class="padThis" id="exampleInputEmoji">
        <div class="setWidth">
        <b-input-group>
            <b-form-input
            class="emojitextinput"
            type="text"
            placeholder="Enter Text Here"
            v-model="valueInput"
            ></b-form-input>
            <b-input-group-append is-text @click="clearInput">
            <i class="fa fa-times moo" aria-hidden="true"></i>
            </b-input-group-append>
            <button @click="toogleDialogEmoji">😃</button>
            <VEmojiPicker
            style="background-color: white"
            class="testbg"
            :emojiWithBorder="false"
            v-show="showDialog"
            :style="{ width: '440px', height: '200' }"
            labelSearch="Search"
            @select="onSelectEmoji"
            />
        </b-input-group>
        </div>
    </div>
</template>

<script>
import { VEmojiPicker } from "v-emoji-picker";

export default {
    name: "emojiComp",
    components: {
        VEmojiPicker,
    },
    data: () => ({
        valueInput: "",
        showDialog: false,
    }),
    methods: {
        toogleDialogEmoji() {
        this.showDialog = !this.showDialog;
        },
        onSelectEmoji(emoji) {
        this.valueInput += emoji.data;
        },
        clearInput() {
        this.valueInput = "";
        },
    },
};
</script>

<style scoped>
.setWidth {
    width: 30%;
}

button {
    border: 1px solid #ced4da;
    border-radius: 0px 5px 5px 0px;
    padding: 0rem 0.4rem;
    background-color: transparent;
}

input {
    border-right: none;
}

.padThis {
    margin: 1rem;
}

.input-group-text {
    background-color: white;
    border: 1px 0px 0px 0px solid white;
}

.moo:hover {
    transform: scale(1.1);
}
</style>