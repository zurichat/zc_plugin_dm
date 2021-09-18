<template>
    <div class="padThis" id="exampleInputEmoji">
        <div class="setWidth">
            <VEmojiPicker
                :emojiWithBorder="false"
                :style="{ width: '440px', height: '200' }"
                labelSearch="Search"
                @select="onSelectEmoji"
                v-show="pickEmoji"
            />
        </div>
    </div>
</template>

/* Instructions for Abisalde --run npm install v-emoji-picker --Add to main.vue
import VEmojiPicker from 'v-emoji-picker'; import { BootstrapVueIcons,
BootstrapVue, IconsPlugin } from 'bootstrap-vue'; */

<script>
import { VEmojiPicker } from 'v-emoji-picker';
import { mapGetters } from 'vuex';

export default {
    name: 'emojiComp',
    components: {
        VEmojiPicker,
    },
    props: ['onSelectEmoji'],
    data: () => ({
        valueInput: '',
        showDialog: false,
    }),
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
    margin: -15rem 0 5rem 3rem;
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
