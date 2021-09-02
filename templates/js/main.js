var app = new Vue({
    el: '#app',
'store': new Vuex.Store(
    {
      state: {
        zuri_messages: {
          message: [
            {
              "id": "001",
              "profile_photo": "user.png",
              "sender": "Romanric",
              "receiver": "Phosah",
              "message": "There will be an urgent meeting with the frontend team today at 8:00pm. Everyone should try to attend. We will be discussing majorly on how best to move the project forward.",
              "delivered": true,
              "media_file": false,
              "has_emoji": true,
              "time": "3:18pm",
            },
            {
              "id": "002",
              "profile_photo": "user.png",
              "sender": "Belrah",
              "receiver": "blac_dev",
              "message": "Hello, Are you busy? We have to continue our discussions on the project. It's mandatory we finish it before our next meeting.",
              "delivered": true,
              "media_file": true,
              "has_emoji": false,
              "time": "10:28am",
            },
            {
              "id": "003",
              "profile_photo": "user.png",
              "sender": "Psami",
              "receiver": "HeizelCodes",
              "message": "Just don't forget to do it. You've been procastinating for so long. It's beginning to seem as if we aren't making any headway",
              "delivered": true,
              "media_file": true,
              "has_emoji": true,
              "time": "6:15am",
            },
            {
              "id": "004",
              "profile_photo": "user.png",
              "sender": "Zxenon",
              "receiver": "Ej",
              "message": "I just finished the first part of the project. Will start work on the rest immediately. Is there any other thing you'd like for me to do? We're behind schedule.",
              "delivered": false,
              "media_file": false,
              "has_emoji": true,
              "time": "4:24pm",
            },
            {
              "id": "005",
              "profile_photo": "user.png",
              "sender": "Geegee",
              "receiver": "Delight",
              "message": "Why are you not picking my calls. You know we have a meeting for 8:00am tommorrow and you're refusing to pick calls. Have you pushed to the repo?",
              "delivered": true,
              "media_file": false,
              "has_emoji": false,
              "time": "8:18pm",
            }
          ]
        }
      },
      mutations: {
      },
      actions:{

      },
      getters:{

      }
    }
  ),
delimiters: ["[[", "]]"],
data: {
  message: 'Hello Vue!',  
},

});