function showIt() {
  document.getElementById('reminder1').style.display = "block";
}

var app = new Vue({
    el: '#reminder',
    data: {
      show: true,
  }

// all these are not needed
// 'store': new Vuex.Store(
//     {
//       state: {
//         // message: 'Welcome, Vuex is now available for this app'
//       },
//       mutations: {
//       },
//       actions:{

//       },
//       getters:{

//       }
//     }
//   ),
// delimiters: ["[[", "]]"],
// data: {
//     // message: 'Hello Vue!'
// },

});