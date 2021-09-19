module.exports = {
    lintOnSave: false,
    configureWebpack: {
        devServer: {
            headers: {
                'Access-Control-Allow-Origin': '*',
            },
            disableHostCheck: true,
            sockPort: 8080,
            sockHost: 'localhost',
            port: 8080,
            hot: true,
        },
        externals: ['vue', 'vue-router', /^@zuri\/.+/],
    },
    filenameHashing: false,
};
