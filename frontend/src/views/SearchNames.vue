<template>
  <div class="view">
    <div class="side-nav"></div>
    <div class="container">
      <div class="content">
        <JumpToUser />
      </div>
    </div>
  </div>
</template>

<script>
import JumpToUser from "../components/jumpToUser.vue";

export default {
  name: "User Search",
  components: {
    JumpToUser,
  },
};
</script>

<style scoped>
.view {
  display: flex;
  flex-direction: row;
  min-height: 100vh;
  min-width: 100vw;
  overflow: hidden;
}

.side-nav {
  border-right: 0.5px solid gray;
  flex: 1/2;
  width: 268px;
  padding: 3px;
}
.content {
  flex: 2;
}
.container {
    background-color: #F6F6F6;
}
</style>