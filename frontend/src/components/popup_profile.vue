<template>
    <div class=" userContainer rounded shadow  bg-white " >
   
          <div class="px-4">
                <b-img class="rounded-circle u_icon" :src="userData.profileImage" ></b-img>
              

            <div style="font-size:23px"><b>{{userData.displayName}}</b></div>
            <div style="font-size:14px">
                {{userData.profession}}<br>
                {{userData.gender}}
                <div class="mt-5"> <a href="/" class="text-decoration-none">View Full Profile</a></div>
          </div>
      
     <div  class="text-muted" >
             <small style="font-size:;margin-top:32px">Status</small><br>
              <!-- <i  class="fa fas fa-cat"></i>     -->

              <img src="@/assets/Emoji.png" style="height:18px; width:18px;"  >   


           <div style="margin:26.18px 0 27px 0;  font-size:13px">
             <div class="text-muted">Local Time </div>
            <div>{{userData.localTime}}</div>
          </div>
          </div> 
            <div class="d-flex justify-content-between mb-3">
                <b-button  size="sm" variant="outline-secondary" class="lh-1">Message</b-button> 
                <b-button size="sm" variant="outline-secondary" class="lh-1">Mute</b-button>
            </div>
           
           
        
      </div>
    </div>
  
</template>

<script>
export default {
   data(){
     return{
       userData:{
         displayName:'Mama Gee',
         profession:'Frontend Desing Mentor',
         gender:'he/her',
         localTime:'3:15PM',
         phoneNumber: '021345789',
         profileImage:require('@/assets/images/mamaGee.jpg')
       }
     }
   }
}
</script>

<style scoped>
    button{
        width:125px;
        height: 32px;
    }
    .primaryColor{
       background-color:#00B87C;
    }
    .userContainer{
        position:absolute;
        z-index: 1;
        width:320px;
        /* min-height: 632px; */
        /* height: 60vh; */
        font-family:'Lato', sans-serif;
        left: 10.5%;
        /* right: 40%; */
    }

    .u_icon{
      width:280px;
      height: 280px;
      margin: 16px 0px 3px -3px;
      object-fit: cover;
    }
    .btn-rounded{
      border-radius:100%;
    }
    
    .profile_icons button{
      height:65%
    }


    </style>