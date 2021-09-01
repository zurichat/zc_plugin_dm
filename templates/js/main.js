var app = new Vue({
    el: '#app',
'store': new Vuex.Store(
    {
      state: {
        message: 'Welcome, Vuex is now available for this app'
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
    message: 'Hello Vue!'
},

});