<template>
    <div class="message-thread mt-4">
        <div class="msgBody">
            <div class="conversation-threads d-flex flex-row">
                <div class="userProfile-avatar">
                    <img src="../assets/Ellipse 21.png" alt="User Image" />
                </div>
                <div class="usertext-messages">
                    <h5 class="pb-2">
                        <span class="userName">MamaGee</span>
                        <span class="msgTime">5.55pm</span>
                    </h5>
                    <p class="text">
                        Lorem ipsum dolor sit, amet consectetur adipisicing
                        elit. Eum mollitia aspernatur laboriosam cum officiis
                        commodi deleniti odit rerum ratione consectetur. Lorem
                        ipsum dolor sit amet, consectetur adipiscing elit.
                        Tincidunt adipiscing et, tortor, fusce quis tellus,
                        enim. A, posuere mi auctor odio tincidunt magnis.
                    </p>
                </div>
            </div>

            <div class="conversation-threads d-flex flex-row">
                <div class="userProfile-avatar">
                    <img src="../assets/Ellipse 24.png" alt="User Image" />
                </div>
                <div class="usertext-messages">
                    <h5 class="pb-2">
                        <span class="userName">Geegee</span>
                        <span class="msgTime">5.57pm</span>
                    </h5>
                    <p class="text">
                        Lorem ipsum dolor sit, amet consectetur adipisicing
                        elit. Eum mollitia aspernatur laboriosam cum officiis
                        commodi deleniti odit rerum ratione consectetur. Lorem
                        ipsum dolor sit amet, consectetur adipiscing elit.
                        Tincidunt adipiscing et, tortor, fusce quis tellus,
                        enim. A, posuere mi auctor odio tincidunt magnis.
                    </p>
                </div>
            </div>

            <div class="conversation-threads d-flex flex-row">
                <div class="userProfile-avatar">
                    <img src="../assets/Ellipse 21.png" alt="User Image" />
                </div>
                <div class="usertext-messages">
                    <h5 class="pb-2">
                        <span class="userName">MamaGee</span>
                        <span class="msgTime">6.05pm</span>
                    </h5>
                    <p class="text">
                        Lorem ipsum dolor sit, amet consectetur adipisicing
                        elit. Eum mollitia aspernatur laboriosam cum officiis
                        commodi deleniti odit rerum ratione consectetur. Lorem
                        ipsum dolor sit amet, consectetur adipiscing elit.
                        Tincidunt adipiscing et, tortor, fusce quis tellus,
                        enim. A, posuere mi auctor odio tincidunt magnis.
                    </p>
                </div>
            </div>

            <div class="conversation-threads d-flex flex-row">
                <div class="userProfile-avatar">
                    <img src="../assets/Ellipse 21.png" alt="User Image" />
                </div>
                <div class="usertext-messages">
                    <h5 class="pb-2">
                        <span class="userName">MamaGee</span>
                        <span class="msgTime">5.55pm</span>
                    </h5>
                    <p class="text">
                        Lorem ipsum dolor sit, amet consectetur adipisicing
                        elit. Eum mollitia aspernatur laboriosam cum officiis
                        commodi deleniti odit rerum ratione consectetur. Lorem
                        ipsum dolor sit amet, consectetur adipiscing elit.
                        Tincidunt adipiscing et, tortor, fusce quis tellus,
                        enim. A, posuere mi auctor odio tincidunt magnis.
                    </p>
                </div>
            </div>

            <div class="conversation-threads d-flex flex-row">
                <div class="userProfile-avatar">
                    <img src="../assets/Ellipse 24.png" alt="User Image" />
                </div>
                <div class="usertext-messages">
                    <h5 class="pb-2">
                        <span class="userName">GeeGee</span>
                        <span class="msgTime">5.57pm</span>
                    </h5>
                    <p class="text">
                        Lorem ipsum dolor sit, amet consectetur adipisicing
                        elit. Eum mollitia aspernatur laboriosam cum officiis
                        commodi deleniti odit rerum ratione consectetur. Lorem
                        ipsum dolor sit amet, consectetur adipiscing elit.
                        Tincidunt adipiscing et, tortor, fusce quis tellus,
                        enim. A, posuere mi auctor odio tincidunt magnis.
                    </p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'DmMesssageThread',
};
</script>

<style scoped>
.conversation-threads {
    margin-bottom: 32px;
}

.userProfile-avatar {
    padding-right: 16px;
}

.userProfile-avatar img {
    vertical-align: middle;
}

.usertext-messages {
    font-size: 14px;
    line-height: 1.8;
}

.usertext-messages h5 {
    margin-bottom: 0;
    font-size: 16px;
    font-weight: 600;
}

.usertext-messages span.msgTime {
    padding-left: 8px;
    font-size: 12px;
    color: #999999;
    font-weight: 400;
}

.usertext-messages p {
    margin-bottom: 0;
}
</style>
