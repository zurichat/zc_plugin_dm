<template>
    <header>
        <div class="dm-profile-header-content d-flex flex-column">
            <div class="avatar-username py-2 px-3">
                <div
                    class="profile-avatar d-flex flex-flow align-items-center"
                    @click="toggle"
                >
                    <div class="dmheader-img-avatar">
                        <img src="https://picsum.photos/200/300" alt="{}" />
                    </div>
                    <h6>
                        <span class="username">Sandra Bernard</span
                        ><b-icon icon="chevron-down"></b-icon>
                    </h6>
                </div>
            </div>

            <div
                class="add-bookmark d-flex flex-flow align-items-center px-3 py-1"
                @click="toggle_bookmark"
            >
                <button class="btn btn-add-bookmark d-flex align-items">
                    <b-icon icon="plus" />
                    <p>Add a bookmark</p>
                </button>
            </div>
        </div>

        <transition name="fade" appear>
            <div class="modal-overlay" v-if="show">
                <div class="pop">
                    <div class="head">
                        <div class="profile_layout">
                            <div class="profile">
                                <div class="dmprofile-img-avatar">
                                    <img
                                        src="https://picsum.photos/200/300"
                                        alt="profile_pic"
                                        class="img"
                                    />
                                </div>
                                <div class="profile_text">
                                    <h1>Mama Gee</h1>
                                    <p>Frontend developer</p>
                                </div>
                            </div>
                            <b-icon
                                icon="x"
                                scale="2"
                                @click="toggle"
                                class="close"
                            ></b-icon>
                        </div>
                        <div class="mute_start_a_call mt-4 d-flex">
                            <b-button class="btn_mute me-2">
                                <b-icon class="close bi bi-bell-slash"></b-icon>
                                Mute
                            </b-button>
                        </div>

                        <div class="switch">
                            <div class="abt">About</div>
                            <div class="int">Integrations</div>
                        </div>
                    </div>
                    <div class="body">
                        <div class="card_1">
                            <div class="mb">
                                <b-icon
                                    icon="clock"
                                    scale="1.3"
                                    class="card_icon"
                                ></b-icon>
                                <span class="text_gray">3:15AM Local Time</span>
                            </div>
                            <div class="mb">
                                <b-icon
                                    icon="telephone"
                                    scale="1.3"
                                    class="card_icon"
                                ></b-icon
                                ><span>+23701877832</span>
                            </div>
                            <div class="mb">
                                <b-icon
                                    icon="envelope"
                                    scale="1.3"
                                    class="card_icon"
                                ></b-icon
                                ><span class="text_blue"
                                    >mamagee@gmail.com</span
                                >
                            </div>
                            <p class="view_profile text_blue">View Profile</p>
                        </div>
                        <div class="card_2">
                            <h1>Files</h1>
                            <p>
                                There aren’t any files to see here. But there
                                could be - drag and drop any file to the message
                                panel to add it to this conversation
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </transition>
        <div class="addBookmark-overlay" v-if="bookmark">
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
                    v-for="item in bookmarks"
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
                        <h2 class="m-0">{{ item.link }}</h2>
                        <p>{{ item.description }}</p>
                    </div>
                </div>
            </div>
        </div>
    </header>
</template>

<script>
// import @/components

export default {
    name: 'DmProfileHeader',
    data() {
        return {
            message: 'Add a bookmark to this channel',
            description: `Easily find your team's important links`,
            show: false,
            bookmark: false,
            bookmarks: [
                {
                    id: 0,
                    link: 'https://dm.zuri.chat/api/v1/sidebar',
                    description: `${'Delight'} - ${'Yesterday'}`,
                },
                {
                    id: 1,
                    link: 'https://dm.zuri.chat/api/v1/sidebar',
                    description: `${'Abisalde'} - ${'Today'}`,
                },
            ],
        };
    },
    methods: {
        toggle: function() {
            return (this.show = !this.show);
        },
        toggle_bookmark: function() {
            return (this.bookmark = !this.bookmark);
        },
    },
};
</script>

<style scoped>
.dm-profile-header-content {
    background: transparent;
}

.dm-profile-header-content .avatar-username {
    background-color: var(--bg-color-header);
}

.dmheader-img-avatar,
.profile-avatar > h6 {
    cursor: pointer;
    outline: none;
    user-select: none;
    color: #ffffff;
}

.dmheader-img-avatar img {
    width: 24px;
    height: 24px;
    border-radius: 4px;
    border: 0.5 solid #ccc;
}

.profile-avatar h6 {
    margin-bottom: 0;
    padding-left: 14px;
    font-weight: 600;
    font-size: 17px;
}

.profile-avatar h6 .bi-chevron-down {
    vertical-align: middle;
    margin-left: 10px;
    font-size: 11px;
}

div.add-bookmark {
    background-color: var(--bg-color-footer);
}

.btn.btn-add-bookmark {
    background-color: var(--color-btn-bookmark);
    border-radius: 4px;
    padding: 4px 10px;
    border: none;
}

.btn.btn-add-bookmark p {
    margin: 0;
    font-size: 13px;
    padding-left: 4px;
}
/* profilepopModal styles */
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 2;
    background-color: rgba(0, 0, 0, 0.45);
}
.pop {
    background: #f6f6f6;
    width: 40%;
    max-width: 45%;
    margin: 2% auto;
    border-radius: 8px;
}
.head {
    background: white;
    padding: 24px 33px 0px;
    border-top-right-radius: 8px;
    border-top-left-radius: 8px;
}
.profile {
    display: flex;
}
.img {
    width: 85px;
    height: 94px;
    border-radius: 6px;
    margin-right: 19px;
}
.profile_layout {
    display: flex;
    justify-content: space-between;
}
.profile_text h1 {
    font-size: 25px;
    font-weight: 700;
    margin-bottom: 6px;
}
.profile_text p {
    font-size: 15px;
    margin-bottom: 3px;
    color: #3a3a3a;
}
.close {
    cursor: pointer;
}
.btn_mute,
.btn_mute:hover {
    border: 1px solid #979797;
    background: transparent;
    border-radius: 6px;
    color: gray;
    font-size: 12px;
    font-weight: 700;
    padding: 9px 20px 9px 15px;
}
.mute {
    margin-right: 9px;
}
.switch {
    display: flex;
    margin-top: 21px;
    font-size: 15px;
}
.abt {
    margin-right: 32px;
    border-bottom: 1px solid #00b87c;
    padding-bottom: 11px;
}
.body {
    padding: 20px 35px;
}
.card_1,
.card_2 {
    background: #ffffff;
    border-radius: 8px;
    font-size: 15px;
}
.card_1 {
    padding: 26px 26px 21px;
    margin-bottom: 21px;
}
.card_icon {
    margin-right: 12px;
}
.mb {
    margin-bottom: 20px;
    text-align: start;
}
.text_gray {
    color: #3a3a3a;
    cursor: pointer;
}
.text_blue {
    color: rgba(0, 97, 195, 0.66);
    cursor: pointer;
}
.view_profile {
    font-weight: 700;
    margin-bottom: 0;
    text-align: start;
}
.card_2 {
    padding: 20px 20px;
}
.card_2 h1 {
    font-size: 15px;
    font-weight: 700;
}
/* bookmark style */
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
    font-weight: 400;
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

ul {
    padding: 0;
    text-align: start;
}

li {
    color: black;
}
.addBookmark-overlay {
    position: absolute;
    right: 5%;
    z-index: 111;
}
</style>
