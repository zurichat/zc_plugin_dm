<template>

    <div class="userContainer shadow bg-white">

        <div     
          class=" header text-white primaryColor d-flex justify-content-between align-items-center px-3 ">
            <h6>Profile</h6>
            
          <div><i class="fa fa-times" aria-hidden="true"></i></div>
        </div>
   
        <div style="height: 5.7vh; background-color: var(--bg-color-footer);"></div>
        <div class="side-profile px-2">
          <div class="text-center">
          <div class="mx-3">
            <b-img class="  u_icon" :src="userData.profileImage"></b-img>
          
          </div>
      
            <div style="font-size:23px"><b>{{userData.displayName}}</b></div>
            
            <div style="font-size:14px">
                {{userData.profession}}<br>
                {{userData.gender}}
          </div>
          
          <i class="my-4 fa fas fa-cat"></i>
           
          </div>
          <div class="profile_icons d-flex justify-content-around mb-2 mx-4">
            <div class="text-center">
              <button class="btn btn-light btn-rounded shadow-sm mb-2">
                <i class="far fa-comment"></i>
              </button>
              <div class="text-muted">Message</div>
            </div>

            <div>
              <button class="btn btn-light btn-rounded shadow-sm mb-2">
                <i class="far fa-bell-slash" aria-hidden="true"></i>
              </button>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              <div class="text-muted">Muted</div>
            </div>
            <div class="text-center">
              <button class="btn btn-light btn-rounded shadow-sm mb-2">
                <i class="fa fa-ellipsis-h"></i>
              </button>
              <div class="text-muted">More</div>
            </div>
          </div>

          <div class="text-left p-3 margin:26.18px 0 27px 0;  font-size:13px">
            <div class="mb-2">
              <div class="text-muted">Display Name</div>
              <div>{{ userData.displayName }}</div>
            </div>

            <div class="mb-2">
              <div class="text-muted">Local Time</div>
              <div>{{ userData.localTime }}</div>
            </div>

            <div class="mb-2">
              <div class="text-muted">Phone Number</div>
              <div>{{ userData.phoneNumber }}</div>
            </div>
          </div>
        </div>
      </div>
  
</template>

<script>
export default {
  data() {
    return {
      userData: {
        displayName: "Mama Gee",
        profession: "Frontend Design Mentor",
        gender: "She/Her",
        localTime: "3:15PM",
        phoneNumber: "0211345789",
        profileImage: "https://picsum.photos/200/300",
      },
    };
  },
};
</script>

<style scoped>
.primaryColor {
  background-color: #00b87c;
}
.userContainer {
 
  width: 19rem;
  height: auto;
  font-family: "Lato", sans-serif;
  grid-column-start: 2;
  grid-column-end: 5;
}
.header{
  height:6.6vh;
  margin-left:10px
}

.userContainer img {
  width: 100%;
  height: 250px;
}
.btn-rounded {
  border-radius: 100%;
}

.profile_icons button {
  height: 65%;
}

.u_icon{
      width:280px;
      height: 380px;
      margin: 16px 0px 16px 6px;
      object-fit: cover;
    }
  
</style>