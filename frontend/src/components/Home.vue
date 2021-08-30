<template>
  <div class="container py-3 border w-50" >
    <h1>Dm plugin vuejs frontend</h1>
    <MessageDisplaySections/>
    <FormSection/>
  </div>
</template>

<script>
import MessageDisplaySections from './MessageDisplaySection.vue'
import FormSection from './FormSection.vue'
export default {
  components:{
    MessageDisplaySections,
    FormSection
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
