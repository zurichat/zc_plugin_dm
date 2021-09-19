const path = require('path');
const fs = require('fs');
const EventHooksPlugin = require('event-hooks-webpack-plugin');

module.exports = {
    lintOnSave: false,
    filenameHashing: false,
    configureWebpack: {
        devServer: {
            headers: {
                'Access-Control-Allow-Origin': '*',
            },
            disableHostCheck: true,
            sockPort: 9090,
            sockHost: 'localhost',
            port: 9090,
            hot: true,
        },
        externals: ['vue', 'vue-router', /^@zuri\/.+/],
        plugins: [
            new EventHooksPlugin({
                done: () => {
                    if (process.env.NODE_ENV !== 'development') {
                        const removeIndexFile = path.join(__dirname, 'dist');
                        fs.unlinkSync(`${removeIndexFile}/index.html`);
                    }
                },
            }),
        ],
    },
};
