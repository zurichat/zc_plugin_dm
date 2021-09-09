<template> 
    <div class="schedule-message-wrapper d-flex">
        <div class="schedule-message-body d-flex flex-column">
            <header class="schedule-text">Schedule message</header>
            <div class="schedule-message-content">
                <p class="time-info">Later today at 9:00 AM</p>
                <p class="time-info">Monday at 9:00 AM</p>
            </div>
                <hr />
                <p class="time-info-custom">Custom time</p>
        </div>
    </div>
</template>


<script>


export default {
    name: 'ScheduleMessageModal',
};
</script>

<style scoped>
.schedule-message-wrapper {
    width: 275px;
    height: auto;
    position: absolute;
    top: 20%;
}

.schedule-message-body {
    width: 100%;
    background-color: #fff;
    border-radius: 5px;

}

header.schedule-text {
    font-size: 13px;
    color: #999999;
    line-height: 1.5;
    padding: 7px 15px 0;
}

.schedule-message-content, .time-info-custom {
    padding: 7px 15px 15px;
}

p.time-info {
    font-size: 15px;
    margin-bottom: 0 !important;
    line-height: 1.75;
    color: #3A3A3A;
}

hr {
    margin: 0;
    border: 1px solid #e7e7e7
}
</style>