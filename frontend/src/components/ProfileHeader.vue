<template>
    <div id="profile-header">
        <div id="profile-icon" @click="toggleProfileInfo">
            <img id="profile-avatar" alt="profile avatar" src="../assets/profileicon.png">
        

        </div>
        <div id="profile-info" v-if="displayProfileInfo">
            <h1 id="profile-h1"> Profile </h1>
            <img id="card" alt="profile card" src="../assets/profilecard.png">
            <h1> Mama Gee </h1>
            <p> Frontend Design Mentor </p>
            <p> She/Her </p><br><br>
            <img id="vector" alt="vector" src="../assets/vector.png">

            



            <p> Display Name </p>
            <p> Mama Gee</p>

            <p> Local Time </p>
            <p> 3:15 PM </p>

            <p> Phone Number </p>
            <p> 0213456789</p>





            
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
        right: 20px;
        top: 5px;
        border-radius: 50%;
    }

    #profile-info{  
        position: absolute;
        right: 5px;
        top: 60px;
        height: 900px;
        width: 300px;
        background-color: white;
     
    
    }

    #profile-avatar{
        position: relative;

    }

    #profile-h1{
        background-color:#00B87C;
        color: white;
        height: 60px;
    

    }
</style>
