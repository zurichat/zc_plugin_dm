<template>
    <div class="padThis" id="exampleInputEmoji">
        <div class="setWidth">
            <Picker
                :data="emojiIndex"
                set="google"
                color="rgb(0, 184, 123)"
                @select="onSelectEmoji"
                v-show="pickEmoji"
            />
        </div>
    </div>
</template>

<script>
import data from 'emoji-mart-vue-fast/data/google.json';
import { Picker, EmojiIndex } from 'emoji-mart-vue-fast';
let emojiIndex = new EmojiIndex(data);
import 'emoji-mart-vue-fast/css/emoji-mart.css';
import { mapGetters } from 'vuex';

export default {
    name: 'emojiComp',
    components: {
        Picker,
    },
    props: ['onSelectEmoji'],
    data() {
        return {
            emojiIndex: emojiIndex,
        };
    },
    computed: {
        ...mapGetters(['pickEmoji']),
    },
};
</script>

<style scoped>
.container-emoji .grid-emojis {
    grid-template-columns: repeat(11, 10%);
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
    margin: 0 0 5rem 3rem;
    position: absolute;
    right: 0;
    top: 0;
}

.input-group-text {
    background-color: white;
    border: 1px 0px 0px 0px solid white;
}

.moo:hover {
    transform: scale(1.1);
}
</style>