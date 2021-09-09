<template>
    <div>
        <div class="d-flex align-items-center justify-content-end">
            <div class="d-flex bod align-items-center search-container">
                <b-form-input
                    class="searchbox"
                    size="sm"
                    v-model="text"
                    placeholder="Search here"
                ></b-form-input>
                <b-icon
                    class="search-icon"
                    icon="search"
                    aria-hidden="true"
                ></b-icon>
            </div>
            <b-icon
                class="settings-icon"
                icon="gear"
                aria-hidden="true"
            ></b-icon>
            <b-img
                class="profile-img"
                src="https://i.postimg.cc/yNy5SmZQ/g-Do-NB-BCkd-E.png"
                rounded="circle"
            ></b-img>
        </div>
    </div>
</template>

<script>
export default {
    name: 'SearchBar',
};
</script>

<style scoped>
.search-container {
    width: 389px;
    position: relative;
}
.settings-icon {
    color: #999999;
    margin-left: 1.5em;
    width: 18px;
    height: 19.18px;
}

.search-icon {
    color: #999999;
    position: absolute;
    right: 12px;
}

.searchbox {
    width: 100%;
    height: 3.35px;
    padding: 0.25em;
    border-radius: 4px;
    background: transparent;
}

.profile-img {
    width: 40px;
    height: 40px;
    margin-left: 1.5em;
}
</style>
