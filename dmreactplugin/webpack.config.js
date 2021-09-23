const { merge } = require('webpack-merge');
const singleSpaDefaults = require('webpack-config-single-spa-react');

module.exports = (webpackConfigEnv, argv) => {
    const defaultConfig = singleSpaDefaults({
        orgName: 'zuri',
        projectName: 'zuri-plugin-dm',
        webpackConfigEnv,
        argv,
    });

    return merge(defaultConfig, {
        // modify the webpack config however you'd like to by adding to this object
        module: {
            rules: [
                {
                    test: /\.css$/i,
                    use: [
                        // Use require.resolve to ensure the correct loader is used
                        require.resolve('style-loader', {
                            paths: [
                                require.resolve('webpack-config-single-spa'),
                            ],
                        }),
                        require.resolve('css-loader', {
                            paths: [
                                require.resolve('webpack-config-single-spa'),
                            ],
                        }),
                        'postcss-loader',
                    ],
                },
            ],
        },
    });
};
