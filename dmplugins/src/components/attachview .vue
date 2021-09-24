<template>
  <div>
       
      <AttachFile class="ease"  v-show='toggle'/>
 <button class="btn btn-primary m-5" ><b-icon icon="paperclip" @click='toggle = !toggle'></b-icon></button>
  </div>
</template>

<script>
import AttachFile from '@/components/attachFile.vue'
export default {
   data() {
    return { 
     toggle: true,
     
    };
  },
components:{
    AttachFile,
}
}
</script>

<style scoped>
.ease{
      transition: 0.5s ease-out;

}

button{
 position:fixed;
  right:2px;
  bottom:2px;
}
</style>