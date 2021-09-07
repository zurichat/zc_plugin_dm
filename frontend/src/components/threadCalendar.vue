<template>
    <div class="thread-calendar text-center">
        <div
            class="d-flex justify-content-between align-items-center  border border-gray-200 rounded-pill px-2 justify-content-center wrapper"
        >
            <p class="date-text">{{ message }}</p>
            <b-button
                variant="white"
                class="btn-outline-disabled"
                @click="toggle"
            >
                <b-icon-chevron-down class="b-icon"></b-icon-chevron-down>
            </b-button>
        </div>
        <div
            class="row p-0 border border-gray-200 rounded days-dropdown list-wrapper"
            v-if="show"
        >
            <ul ps-0 p0 m-0>
                <span class="px-3">jump to...</span>
                <li
                    class="my-2 px-3 btn-outline-primary"
                    v-for="day in days"
                    :key="day.id"
                >
                    {{ day.day }}
                </li>
                <hr />
                <li class="my-2 px-3 ">jump to a specific date</li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ThreadCalendar',
    data() {
        return {
            message: 'Monday, August 23rd',
            show: false,
            days: [
                { id: 0, day: 'Today' },
                { id: 1, day: 'Last week' },
                { id: 2, day: 'Last month' },
                { id: 3, day: 'The very beginning' },
            ],
        };
    },
    methods: {
        toggle: function() {
            return (this.show = !this.show);
        },
    },
};
</script>

<style scoped>
.thread-calendar {
    position: relative;
    margin: 0 auto;
    width: 169px;
}

p.date-text {
    margin-bottom: 0 !important;
    font-size: 14px;
    font-weight: 500;
    line-height: 1.75;
    color: #3a3a3a;
}

.b-icon:hover {
    outline: none;
    user-select: none;
}

.b-icon {
    user-select: none;
    outline: none;
    outline-color: transparent;
    font-weight: 600;
}
.b-icon:focus {
    user-select: none;
    outline: none;
    outline-color: transparent;
}

.btn {
    font-size: 9px;
    padding: 0 !important;
}

.btn:focus {
    outline: none;
    outline-color: transparent;
}

span {
    font-size: 15px;
    color: gray;
}
.days-dropdown {
    box-shadow: 0px 8px 30px 1px rgba(0, 0, 0, 0.1);
}

.list-wrapper {
    position: absolute;
    top: 105%;
    left: 6.5%;
    width: 275px;
    background: #ffffff;
}

ul {
    padding: 0;
    text-align: start;
}

li {
    color: black;
}
</style>
