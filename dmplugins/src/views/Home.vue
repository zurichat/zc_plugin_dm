<template>
    <div>
        <component
            v-bind:is="component"
            v-on:changePage="changePg($event)"
        ></component>
    </div>
</template>

<script>
import SearchDirectMessage from './searchDmEntry.vue';
import StartDirectMessage from './startDirectMessage.vue';

export default {
    components: {
        SearchDirectMessage: SearchDirectMessage,
        StartDirectMessage: StartDirectMessage,
    },
    data() {
        return {
            component: StartDirectMessage,
        };
    },
    methods: {
        changePg: function(nextPage) {
            this.component = nextPage;
        },
    },
};
</script>

<style scoped></style>
