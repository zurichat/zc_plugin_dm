<template>
    <div id="profile-header">
        <div id="profile-icon" @click="toggleProfileInfo">
            <img id="profile-avatar" alt="profile avatar" src="../assets/profileicon.png">
        

        </div>

        <div id="profile-info" v-if="displayProfileInfo">
            <div id="profile-card">

                 <h5 id="profile-h1"> Profile </h5>
               
                    <i class="fa fa-times" aria-hidden="true"></i>
                
                
            </div>

                <div>
                    <img id="profileimg" alt="profile image" src="../assets/profileimg.png">
                </div>

                    <div id="user-details">

                        <h4> Mama Gee </h4>
                             <p> Frontend Design Mentor </p>
                        <p> She/Her </p>

                         <i  class="my-4  fa fas fa-dog"></i>

                    </div>
          

        <div id="bookmark">
            <div class="text-muted"> 
                <button class="btn btn-light btn-rounded shadow-sm mb-2">
                <i class='far fa-comment'></i>
                </button><br>
                Message
            </div>

            <div class="text-muted"> 
                <button class="btn btn-light btn-rounded shadow-sm mb-2">
            <i class="far fa-bell-slash" aria-hidden="true"></i>
          </button><br>
                Muted
            </div>

            <div class="text-muted"> 
               <button class="btn btn-light btn-rounded shadow-sm mb-2">
                 <i class="fa fa-ellipsis-h"></i>
                </button> <br>
                More
            </div>
 


        </div><br><br>



        <div class="info">
            <p class="text-muted"> Display Name <br> Mama Gee </p>
        

            <p class="text-muted"> Local Time <br>  3:15 PM  </p>
            

            <p class="text-muted"> Phone Number <br>  0213456789 </p>
        
        </div>




            
        </div> 

    </div> 
    

</template>

<script>
export default {
    name:'ProfileHeader',
    setup() {
        
   
    },
    data(){
        return {
            displayProfileInfo: false
        }
    },
    methods:{
        toggleProfileInfo(){
            if (this.displayProfileInfo) 
            {
                this.displayProfileInfo = false;
            } else {
                this.displayProfileInfo = true;
            }
        }


   }
}
</script>

<style scoped>
    #profile-icon{
        position: absolute;
        right: 19px;
        top: 18px;
        border-radius: 50%;
    }

    #profile-info{  
        position: absolute;
        right: 3px;
        top: 60px;
        height: 900px;
        width: 320px;
        background-color: white;
        font-family:'Lato', sans-serif;
     
    
    }

    #profile-avatar{
        position: relative;

    }

    #profile-card{
    
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 2;
        background-color: #00B87C;
        color: white;
        height: 60px;
    }

    #user-details{
       text-align: center;

    }

    #info{
        text-align: left;
        
    }

    #bookmark{
        display: flex;
        justify-content: space-between;
    }


            
</style>
