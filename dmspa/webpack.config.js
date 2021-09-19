const { merge } = require('webpack-merge');
const singleSpaDefaults = require('webpack-config-single-spa');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = (webpackConfigEnv, argv) => {
    const orgName = 'zuri';
    const defaultConfig = singleSpaDefaults({
        orgName,
        projectName: 'root-config',
        webpackConfigEnv,
        argv,
        disableHtmlGeneration: true,
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
        plugins: [
            new HtmlWebpackPlugin({
                inject: false,
                template: 'src/index.ejs',
                templateParameters: {
                    isLocal: webpackConfigEnv && webpackConfigEnv.isLocal,
                    orgName,
                },
            }),
        ],
    });
};
