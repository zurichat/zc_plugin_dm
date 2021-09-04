//divider component
Vue.component("divider", {
    props: [],
    template:
        '<div class="divider-line border-top"><div class="btn py-1 timeline border position-relative">Wednesday, 1st September <span class="chevron d-inline-block">&#x203A;</span></div></div>',
});

// Message Ccomponent
Vue.component("ind-message", {
    template: `<div>
      <div class="d-flex flex-wrap-xs align-items-start bg-light p-2" v-for="(messages, index) in message_data" >
              <img class="rounded-circle message_user_icon" style="border:2px" :src="messages.user_icon">
              <div>
                  <b>{{messages.user_name}}</b>&nbsp;&nbsp;{{messages.time_stamp}}
                  <div>
                      {{messages.main_message}}
                  </div>
              </div>
          </div>
      </div>`,
    data: function () {
        return {
            message_data: [
                {
                    user_name: "MammaGee",
                    user_icon: "images/big.jpg",
                    main_message:
                        "Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque natus magni consequuntur aut ducimus odit veniam voluptatum necessitatibus! Ipsum eum voluptates neque ipsa, reiciendis distinctio hic aliquid blanditiis vel iusto.",
                    time_stamp: "5:55pm",
                },
            ],
        };
    },
});
// User sidebar profile
Vue.component("user-sidebar-profile", {
    template: `<div>
<b-button v-b-toggle.sidebar-1>View full profile</b-button>
<b-sidebar id="sidebar-1" title="Profile" right bg-variant="white"> 
 <div slot="header" id="header">
   <b-row>
     <b-col md="10">
       Profile
     </b-col>
     <b-col>
       <p class=""><b-icon icon="x" class=""></b-icon></p>
     </b-col>
   </b-row>
    
</div>
   <b-avatar src="https://avataaars.io/?avatarStyle=Transparent&topType=LongHairDreads&accessoriesType=Round&hairColor=BrownDark&facialHairType=Blank&clotheType=ShirtCrewNeck&clotheColor=Blue03&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Smile&skinColor=Black" size="18rem"></b-avatar>
   <b-card-title class="text-center">Mama Gee</b-card-title>
   <b-card-text class="text-center">Full stack web developer</b-card-text>
   <b-card-text class="text-center">She/Her</b-card-text>
   <p class="h5 mb-2 text-center"><i class="fab fa-wolf-pack-battalion text-center"></i></p>
   
     <b-row>
      <b-col>
        <b-row><p class="h2 mb-2 text-center rounded-circle"><b-icon icon="chat-text" class="rounded-circle p-2" style="background-color: #F6F6F6;"></b-icon></p></b-row>
        <b-row><b-card-sub-title class="h6 text-center">Message</b-card-sub-title></b-row>     
      </b-col>
      <b-col></b-col>
      <b-col></b-col>

    </b-row>
</b-sidebar>
</div>`,
    data: function () {
        return {
            data() {
                return {
                    user_name: "MammaGee",
                    user_avatar:
                        "https://avataaars.io/?avatarStyle=Transparent&topType=LongHairDreads&accessoriesType=Round&hairColor=BrownDark&facialHairType=Blank&clotheType=ShirtCrewNeck&clotheColor=Blue03&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Smile&skinColor=Black",
                };
            },
        };
    },
    // delimiters: ["[[", "]]"],
});