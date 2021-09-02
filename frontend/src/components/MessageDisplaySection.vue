<template>
  <b-container class="w-90 border mb-4">
    <!-- this is the message display section, this section is to  conatain chat between the two persons -->
    <h2>message display section</h2>
    <b-row>
      <b-col class="col-md-8 align-self-start">
        <div class="message">
          <p>this is a test message</p>
          <div class="card" v-for="message in messages" :key="message.user">
            <!-- Loop through the messages array -->
            <div class="card-content">
              <div class="content">
                {{ message.message }}
                <!-- Print the message text-->
              </div>
            </div>
          </div>
        </div>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import axios from "axios";
export default {
  name: "MessageDisplaySection",
  data() {
    return {
      messages: [], // Array for holding the messages
    };
  },
  mounted() {
    // This will be called when MessageDisplaySection is loaded
    this.getMessages(); // Call our getMessages function below
  },
  methods: {
    getMessages() {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/messages",
      }).then((response) => {
          this.messages = response.data;
        console.log(response.data);
      });
    },
  },
};
</script>

<style>
</style>