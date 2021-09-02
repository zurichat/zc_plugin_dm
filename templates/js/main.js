var app = new Vue({
    el: '#app',
'store': new Vuex.Store(
    {
      state: {
        message: 'Welcome, Vuex is now available for this app',
        zuri_messages: {
        zuri_message: [
          {
            "senderName": "Romanric",
            "receiverName": "Phosah",
            "HasProfileImage": false,
            "text": "Hello, Are you busy? We have to continue our discussions on the project. It's mandatory that we finish it before our next meeting",
            "hasEmoji": true,
            "time": "6:03pm",

          },
          {
            "senderName": "Eniola",
            "receiverName": "Thomas",
            "HasProfileImage": true,
            "text": "Just don't forget to do it. You've been procastinating for so long. It's beginning to seem as if we aren't making any headway",
            "time": "9:33pm"
          },
          {
            "senderName": "Jane",
            "receiverName": "Tessy",
            "HasProfileImage": false,
            "hasEmoji": true,
            "text": "Goodmorning dear, Hope your day is going well. I'd like to inform on the impromptu travel for next week. I'm very sorry its coming late but its really urgent and i promise to caught up on work",
            "time": "7:45am"
          },
          {
            "senderName": "Timi",
            "receiverName": "Mark",
            "HasProfileImage": false,
            "hasEmoji": false,
            "text": "With regards to the message you sent i'd let to find out my options. Is it possible i work in both departments or i make a choice and stick to my fort point?",
            "time": "8:15pm"
          },
          {
            "senderName": "Belrah",
            "receiverName": "Jane",
            "HasProfileImage": false,
            "hasEmoji": true,
            "text": "Why are you not picking my calls. You know we have a meeting for 8:00am tommorrow and you're refusing to pick calls. Have you pushed your project?",
            "time": "10:10pm"
          },
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