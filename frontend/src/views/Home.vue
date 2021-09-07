<template>
    <div class="home">
        <b-row class="all-contents">
            <b-col cols="3" class="zurichat-sidebar">
                <div class="hedaer-contents">
                    <p>
                        Lorem ipsum dolor, sit amet consectetur adipisicing
                        elit. Obcaecati officia iure corrupti, perferendis a
                        laudantium earum neque tempora facere ipsum dolore
                        commodi laboriosam temporibus. Repellat omnis vitae
                        inventore. Qui, itaque!
                    </p>
                    <p>
                        Lorem ipsum dolor sit amet consectetur adipisicing elit.
                        Ipsam tempora id iusto necessitatibus reiciendis enim
                        repudiandae numquam porro quam ut. Exercitationem labore
                        totam nihil eius, corporis quam eligendi a! Veritatis!
                    </p>
                </div>
            </b-col>
            <b-col cols="9" class="zurichat-contents-plugin main px-4">
                <header>
                    <div class="searchform-settings-profile py-3">
                        <SearchBar />
                    </div>
                </header>
                <div class="user-profile-header">
                    <DmProfileHeader />
                </div>

                <div class="dm-plugin-contents">
                    <DmPluginContents />
                </div>
            </b-col>
        </b-row>
    </div>
</template>

<script>
// @ is an alias to /src
import SearchBar from '@/components/searchBar.vue';
import DmProfileHeader from '@/components/dmProfileHeader.vue';
import DmPluginContents from '@/components/dmPluginContents.vue';

export default {
    name: 'Home',
    components: {
        SearchBar,
        DmProfileHeader,
        DmPluginContents,
    },
};
</script>

<style scoped>
.hone .all-contents {
    position: relative;
    width: 100%;
}

.zurichat-sidebar {
    background: #fff;
    overflow-x: hidden;
}

.zurichat-contents-plugin {
    position: relative;
    background: #f6f6f6;
}

.user-profile-header {
    margin: 16px 0 26px;
}

dm-plugin-contents {
    position: relative;
}

@media screen and (min-width: 100px) and (max-width: 767px) {
    .all-contents .zurichat-sidebar {
        position: sticky;
        top: 0;
        left: 0;
        width: 100%;
        overflow: auto;
    }

    .all-contents .zurichat-contents-plugin {
        width: 100%;
    }
}
</style>
