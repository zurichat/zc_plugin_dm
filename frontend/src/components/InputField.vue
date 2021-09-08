<template>
  <div class="border border-gray-300 rounded mx-2">
  <b-input-group class="mt-3 text-input">
    <b-form-input placeholder="Send Message to" class="py-2" v-model="this.sendMsg" style="border: none;"></b-form-input>
  </b-input-group>
  <div class="emoji-group">
      <div class="">
      <span class="light">
        <b-icon icon="lightning" aria-hidden="true" class="border-right-2"></b-icon>
      </span>
      <b-icon icon="type-bold" aria-hidden="true"></b-icon>
      <b-icon icon="type-italic" aria-hidden="true"></b-icon>
      <b-icon icon="type-underline" aria-hidden="true"></b-icon>
      <b-icon icon="code-slash" aria-hidden="true"></b-icon>
      <b-icon icon="link" aria-hidden="true"></b-icon>
      <b-icon icon="list-ul" aria-hidden="true"></b-icon>
      <b-icon icon="file-earmark-code" aria-hidden="true"></b-icon> 
    </div>
      <div>
      <!-- The font-size icon was not found in the bootstrap icon -->
      <b-icon icon="at" aria-hidden="true"></b-icon>
      <b-icon icon="emoji-smile" aria-hidden="true"></b-icon>
      <b-icon icon="paperclip" rotate="45" aria-hidden="true"></b-icon>
      <span class="send">
        <b-icon icon="arrow-right-circle" aria-hidden="true"></b-icon>
        <span class="divider"></span>
        <b-icon icon="chevron-down" aria-hidden="true"></b-icon>
      </span>
    </div>  
  </div>
  </div>
</template>

<script>
export default {
    data() {
        return {
          message: 'Hello',
          sendMsg :'',
        }
      }
}
</script>

<style>
    .form-control:focus {
    border-color:transparent ;
    box-shadow:none;
  }
  .light{
    padding-right: 8px;
    border-right: 2px solid black;
  }
  .emoji-group{
    display: flex;
    justify-content: space-between;
    padding: 12px 24px;
    padding-left: 5px;
    cursor: pointer;
}
.b-icon.bi {
  margin: 0px 5px;
}
.send{
  background-color: #00B87C;
  padding: 4px 2px;
  margin-left:4px ;
  color: white;
}
.divider{
  padding: 0px 4px;
  border-right: 2px solid white;
}
</style>