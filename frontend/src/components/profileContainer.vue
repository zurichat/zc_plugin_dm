<template>
  <div>
    <div class=" userContainer rounded shadow-sm m-2 bg-white " >
      <div class="text-center">
          <div class="header text-white primaryColor d-flex justify-content-between align-items-center p-3">
            <h5>Profile</h5>  
            <div><i class="fa fa-times" aria-hidden="true"></i></div>        
          </div>
          <div class="icon m-4">
             <b-img class="rounded-circle" :src="userData.profileImage" ></b-img>
          </div>
          <div>
            <h4><b>{{userData.displayName}}</b></h4>
            <div>{{userData.profession}}</div>
            <div>{{userData.gender}}</div>
          </div>
          <i  class="my-4  fa fas fa-cat"></i>
         
        <div class="profile_icons d-flex justify-content-around mb-4">
        <div class="text-center">
          <button class="btn btn-light btn-rounded shadow-sm mb-2">
            <i class='far fa-comment'></i>
          </button>
          <div class="text-muted ">Message</div>
        </div>
        
        <div>
          <button class="btn btn-light btn-rounded shadow-sm mb-2">
            <i class="far fa-bell-slash" aria-hidden="true"></i>
          </button>
           <div class="text-muted ">Muted</div>
         
        </div>
        <div>
          <button class="btn btn-light btn-rounded shadow-sm mb-2">
             <i class="fa fa-ellipsis-h"></i>
          </button>   
           <div class="text-muted ">More</div>
        </div>
 
        </div>

      </div>
      
        <div class="text-left p-3">
          <div class="mb-2">
             <div class="text-muted">Display Name </div>
            <div>{{userData.displayName}}</div>
          </div>

           <div class="mb-2">
             <div class="text-muted">Local Time </div>
            <div>{{userData.localTime}}</div>
          </div>

           <div class="mb-2">
             <div class="text-muted">Phone Number </div>
            <div>{{userData.phoneNumber}}</div>
          </div>
           
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

    .primaryColor{
       background-color:#00B87C;
    }
    .userContainer{
        position:absolute;
        width:18rem;
        min-height: 100vh;
        font-family:'Lato', sans-serif;
    }
    
    .userContainer img{
      width:100%;
      height: 40vh;
    }
    .btn-rounded{
      border-radius:100%;
    }
    
    .profile_icons button{
      height:65%
    }


    </style>