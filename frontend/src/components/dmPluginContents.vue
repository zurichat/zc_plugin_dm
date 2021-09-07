<template>
    <div class="all-dm-messages py-3 px-4">
        <ThreadCalendar />
        <DmMessageThread />
    </div>
</template>

<script>
import DmMessageThread from '../components/messageThread.vue';
import ThreadCalendar from '../components/threadCalendar.vue';

export default {
    name: 'DmPluginContents',
    components: {
        DmMessageThread,
        ThreadCalendar,
    },
};
</script>

<style scoped>
.all-dm-messages {
    background: #fff;
    margin-bottom: 24px;
}
</style>
