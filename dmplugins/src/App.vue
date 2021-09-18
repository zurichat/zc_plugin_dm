<template>
    <div id="app">
        <router-view />
    </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Lato:wght@100;300;400;700;900&display=swap');
*,
*:before,
*:after {
    box-sizing: border-box;
    padding: 0;
    margin: 0;
    font-family: 'Lato', sans-serif;
}

:root {
    --bg-color-header: #00b87c;
    --bg-color-footer: #e1fdf4;
    --color-btn-bookmark: #bcf9e6;
    --color-hover-send: #1264a3;
}

li {
    list-style: none;
}

a {
    text-decoration: none;
}

p {
    font-size: 15px;
}

div,
main,
article,
section,
header,
nav,
footer,
aside {
    display: block;
}

img {
    vertical-align: middle;
}

#app {
    overflow: hidden;
}
</style>
