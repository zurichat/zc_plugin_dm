<template>
<div id="app">
  <div class="box">
<h5>Add a bookmark</h5>
<div>
<label for="text" class="form-label-1">Link</label>
<input type="text" class= "linkbox" placeholder="|https://docs.acme.com">
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>

<label for="text" class="form-label-2">Name</label>
<input type="text" class="namebox" placeholder=" &#xf0c1; &#xf107; |Ex. Project tracker" style="font-family:Arial, FontAwesome" />

  </div>
<button class="cancel"><p>Cancel</p></button>
<button class="add"><p>Add</p></button>
  </div>
</div>
</template>

<script>

export default {
  name: 'App',

}
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.box{
  position: absolute;
  width: 350px;
  height: 300px;
  left: 445px;
  top: 318px;
  background: #FFFFFF;
  box-shadow: 0px 10px 30px rgba(0,0,0,0.14);
  border-radius: 5px; 
}
h5{
position: absolute;
width: 154px;
height: 25px;
font-family: Lato;
font-style: normal;
font-weight: bold;
font-size: 21px;
line-height: 25px;
color: #1D1D1D;
margin-left: 20px;
margin-top: 10px;
}

.form-label-1{
  position: absolute;
  font-family: lato;
  font-style: normal;
  font-weight: 500;
  line-height: 18px;
  font-size: 15px;
  top:45px;
  margin-left: -150px;
}
.linkbox{
position: absolute;
width: 302px;
height: 41px;
background: #FFFFFF;
border: 1px solid #999999;
box-sizing:border-box;
border-radius: 5px;
margin-top: 70px;
margin-left: -152px;
}

.form-label-2{
position: absolute;
  font-family: lato;
  font-style: normal;
  font-weight: 500;
  line-height: 18px;
  font-size: 15px;
  top:130px;
  margin-left: -152px;
}

.namebox{
position: absolute;
width: 302px;
height: 41px;
background: #FFFFFF;
border: 1px solid #999999;
box-sizing:border-box;
border-radius: 5px;
margin-top: 160px;
margin-left: -152px;
}
button{
  margin-top: 240px;
  margin-inline-end: 0.7em;
}

.add{
background: #00B87C;
border-radius: 3px;
position:absolute;
padding: 3px 18px;
flex-direction: row;
justify-content: center;
align-items: center;
display: inline-block;
margin-left: 90px;
border: 1px solid white
}

.cancel{
  background: #FFFFFF;
border-radius: 3px;
position:absolute;
padding: 3px 18px;
flex-direction: row;
justify-content: center;
align-items: center;
display: inline-block;
margin-left: 0px;
border: 1px solid #00B87C ;
}
.cancel p{
  color: #00B87C;
}

.add p{
  color: white;
}

</style>
