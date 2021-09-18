module.exports = {
    configureWebpack: {
        externals: ['vue', 'vue-router', /^@zuri\/.+/],
    },
};
