<template>
  <div class="container">
    <div class="search-bar">
      <SearchBar />
    </div>
    <div class="body">
      <h5 class="header">All direct messages</h5>
      <br /><br />
      <div>
        <b-form-input
          v-model="text"
          placeholder="To:"
          class="jump_to_user-container"
        ></b-form-input>
      </div>
      <div class="search-results scroll">
        <ul class="users">
          <li class="user-list-active">Amos Mogaka</li>5
          <li class="user-list">Amos Mogaka</li>
          <li class="user-list">Amos Mogaka</li>
          <li class="user-list">Amos Mogaka</li>
          <li class="user-list">Amos Mogaka</li>
          <li class="user-list">Amos Mogaka</li>
          <li class="user-list">Amos Mogaka</li>
          <li class="user-list">Amos Mogaka</li>
          <li class="user-list">Amos Mogaka</li>
          <li class="user-list">Amos Mogaka</li>
          <li class="user-list">Amos Mogaka</li>
          <li class="user-list">Amos Mogaka</li>
          <li class="user-list">Amos Mogaka</li>
          <li class="user-list">Amos Mogaka</li>
          <li class="user-list">Amos Mogaka</li>
          <li class="user-list">Amos Mogaka</li>
        </ul>
      </div>
      <!-- <div class="searched-container">
        <div class="searched">
          <div class="day"><h4>Yesterday</h4></div>
        </div>
        <div class="searched">
          <div class="day"><h4>Yesterday</h4></div>
        </div>
        <div class="searched">
          <div class="day"><h4>Yesterday</h4></div>
        </div>
        <div class="searched">
          <div class="day"><h4>Yesterday</h4></div>
        </div>
        <div class="searched">
          <div class="day"><h4>Yesterday</h4></div>
        </div>
      </div> -->
    </div>
  </div>
</template>

<script>
import SearchBar from "./searchBar.vue";
export default {
  name: "JumpToUser",
  components: {
    SearchBar,
  },
};
</script>

<style scoped>
.search-bar {
  height: 50px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 0px;

  position: absolute;
  width: 493.2px;
  height: 40px;
  left: 850px;
  top: 9px;
}
.searched {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  padding: 20px;

  position: absolute;
  width: 1050px;
  height: 121px;
  left: 296px;
  top: 176px;

  /* Background Color / White */
  background: #ffffff;
  border-radius: 3px;
}
.searched-container {
  overflow-y: scroll;
}
.user-list-active {
  position: absolute;
  width: 95%;
  height: 33px;
  overflow-x: hidden;
  color: white;
  /* Primary Color / Green */

  background: #00b87c;
}
.user-list {
  color: black;
}
.search-results {
  position: absolute;
  width: 800px;
  height: 279px;
  left: 350px;
  top: 139px;
  overflow-y: scroll;
  /* Background Color / White */

  background: #ffffff;
  /* Background Color / White */

  border: 1px solid transparent;
  box-sizing: border-box;
  border-radius: 3px;
}
.user-list-active {
    margin-bottom: 10px;
}
ul li {
  margin-bottom: 10px;
  margin-left: 0;
}
.header {
  position: absolute;
  width: 176px;
  height: 25px;
  left: 296px;
  top: 53px;

  /* Typography 21/ Regular H5 */

  font-family: Lato;
  font-style: normal;
  font-weight: normal;
  font-size: 21px;
  line-height: 25px;

  /* Text Color / Body copy and Icon color */

  color: #3a3a3a; /*  */
}
.jump_to_user-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 20px;

  position: absolute;
  width: 1050px;
  height: 58px;
  left: 296px;
  top: 94px;
  border: 0.5px solid transparent;
  /* Background Color / White */

  background: #ffffff;
  border-radius: 3px;
}
#search-user {
  width: fit-content;
}
.search-results::-webkit-scrollbar {
  width: 6px;
}

.search-results::-webkit-scrollbar-track {
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
  border-radius: 10px;
}

.search-results::-webkit-scrollbar-thumb {
  border-radius: 10px;
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.5);
}
</style>