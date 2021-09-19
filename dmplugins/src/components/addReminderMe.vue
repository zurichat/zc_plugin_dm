<template>
    <div class="wrapper">
        <b-container class="container d-flex p-3">
            <h4 class="header">Create a reminder</h4>
            <div class="date-wrapper">
                <h6 class="header align-self-start d-flex">When</h6>
                <b-datepicker class="dates"></b-datepicker>
            </div>
            <div class="time-wrapper">
                <h6 class="pt-2 align-self-start d-flex">Time</h6>
                <b-timepicker show-seconds></b-timepicker>
            </div>
            <div class="note-wrapper">
                <h6 class="pt-2 align-self-start d-flex">
                    Add a note <em>(optional)</em>
                </h6>
                <b-textarea placeholder="Add a note"></b-textarea>
            </div>
            <div class="button-wrapper mt-5 mb-2">
                <b-button class="cancel" v-on:click="isHidden">cancel</b-button>
                <b-button class="create ml-2" v-on:click="addReminder()"
                    >create</b-button
                >
            </div>
        </b-container>
    </div>
</template>

<script>
export default {
    name: 'HelloWorld',
    props: {
        msg: String,
    },
    data() {
        return {
            isHidden: false,
        };
    },
    methods: {
        async addReminder() {
            const rawResponse = await fetch('', {
                method: 'POST',
                headers: {
                    Accept: 'application/json',
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    date: '',
                    time: '',
                    note: '',
                }),
            });
            const content = await rawResponse.json();
            console.log(content);
        },
        exit() {},
    },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
    height: fit-content;
    width: 450px;
    position: absolute;
    top: 118px;
    right: 0;
    left: 0;
    flex-direction: column;
    background: #fff;
    border-radius: 4px;
}
.header {
    align-self: flex-start;
}
.wrapper {
    min-height: 100vh;
    width: 100%;
    background: rgba(64, 79, 74, 0.13);
}
.dates {
    color: #00b87c;
}
.button-wrapper {
    display: flex;
    align-self: flex-end;
}
.create {
    width: 147px;
    background-color: #00b87c;
    border: 1px solid transparent;
    border-radius: 4px;
}
.cancel {
    width: 147px;
    background-color: #fff;
    color: #000;
    border-radius: 4px;
}
</style>
