<template>
    <div>
        <div class="container mx-auto pt-3 pb-3 addBookmark">
            <div class="row d-flex pt-2 pb-2 mb-3 wrapper">
                <div class="col-auto align-self-center link-btn">
                    <button
                        variant="white"
                        class="col-auto p-2 btn-outline-disabled"
                    >
                        <b-icon-link-45deg
                            scale="1"
                            class="b-icon btn-icon"
                        ></b-icon-link-45deg>
                    </button>
                </div>
                <div class="col bookmark_description ps-0">
                    <h2 class="m-0">{{ message }}</h2>
                    <p>{{ description }}</p>
                </div>
            </div>
            <hr />
            <span class="">Add recent</span>
            <div
                class="row d-flex pt-2 pb-2 mb-3 wrapper"
                v-for="item in days"
                :key="item.id"
            >
                <div class="col-auto align-self-center link-btn">
                    <button
                        variant="white"
                        class="col-auto p-2 btn-outline-disabled"
                    >
                        <b-icon-link-45deg
                            scale="1"
                            class="b-icon btn-icon"
                        ></b-icon-link-45deg>
                    </button>
                </div>
                <div class="col bookmark_description ps-0">
                    <h2 class="m-0">{{ item.id }}</h2>
                    <p>{{ item.day }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'bookmark',
    data() {
        return {
            message: 'Add a bookmark to this channel',
            description: `Easily find your team's important links`,
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
* {
    list-style: none;
    margin: 0;
    padding: 0;
}
button {
    border: none;
    border-radius: 5px;
    outline: none;
}
.wrapper:hover {
    background-color: rgba(0, 97, 195, 0.66);
}
.b-icon {
    outline: none;
    outline-color: transparent;
}
.bookmark_description > p {
    text-align: start;
    font-size: 0.8rem;
    color: gray;
}
.bookmark_description > h2 {
    text-align: start;
    font-size: 1rem;
    font-weight: 600;
}
.addBookmark {
    max-width: 400px;
    width: 35vw;
    background-color: #ffff;
    border-radius: 10px;
    box-shadow: 0px 8px 30px 1px rgba(0, 0, 0, 0.1);
}
.white {
    color: white;
}
span {
    font-size: 15px;
    color: gray;
    text-align: start;
}
</style>
