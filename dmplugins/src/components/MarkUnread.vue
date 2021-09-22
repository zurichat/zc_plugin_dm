<template>
  <div class="hello">
     <b-card no-body style="max-width: 306px; max-height: 378px" id="card">
      <b-list-group flush id="content-group">
        <b-list-group-item id="content">
          Turn off notifications for replies
        </b-list-group-item>
        <b-list-group-item id="content" class="content" v-on:click="fetchText()">
          Mark unread
          <span class="icons" style="float: right" bold>U</span>
        </b-list-group-item>
        <b-list-group-item id="content">
          Remind me about this
          <b-icon
            icon="chevron-right"
            class="icons"
            style="float: right"
            old
          ></b-icon>
        </b-list-group-item>
        <b-list-group-item id="content">Copy link</b-list-group-item>
        <b-list-group-item id="content">
          Pin to this conversation
          <span class="icons" style="float: right" bold>P</span>
        </b-list-group-item>
        <b-list-group-item id="content">
          Edit Messages
          <span class="icons" style="float: right" bold>E</span>
        </b-list-group-item>
        <b-list-group-item id="content">
          <b-icon
            icon="bar-chart-fill"
            class="icons"
            style="float: left"
            bold
          ></b-icon>
          Turn question into poll</b-list-group-item>
        <b-list-group-item id="content">
          More message shortcut
          <b-icon
            icon="box-arrow-up-right"
            class="icons"
            style="float: right"
            bold>
            </b-icon>
        </b-list-group-item>
      </b-list-group>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "MarkUnread",
  data(){
    return{
      // Api: 'https://dm.zuri.chat/api/v1/614841d6e4b2aebf8ec8c8dc/read/new/',
      Api: 'https://dog.ceo/api/breeds/image/random'
      }
    },
      methods:{
        fetchText: async function(){
          let response = await fetch(this.Api, {
            method: 'PUT'
          });
          let data = await response.text();
          // console.log(data)
          document.write(data)
        }
    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Lato:wght@100;300;400;700;900&display=swap");
#card {
  font-family: "Lato";
  text-align: left;
  color: #454545;
  background-color: #f8f8f8;
  box-shadow: 1px 1px 2px 2px #c5c4c48e;
  border-radius: 8px;
  font-weight: 500;
  font-size: 14px;
}
#card #content-group #content {
  z-index: 1;
}
#card #content-group #content .icons{
  width: 18px;
  height: 18px;
  float: right;
  color: #999999;
}
#card #content-group #content:hover {
  height: 1.81rem;
  display: inline-table;
  cursor: pointer;
  background-color: #1264a3;
  color: white;
  justify-items: center;
  align-content: center;
  align-items: center;
  font-size: 14px;
}
#card #content-group #content:nth-child(2),
#card #content-group #content:nth-child(7) {
  border: none;
}
</style>
