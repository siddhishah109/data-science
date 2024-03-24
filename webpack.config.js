const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
    path: path.resolve("build"),
    filename: 'index.js',
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        },
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
    //   {
    //     test: /\.svg$/,
    //     use: ['@svgr/webpack'],
    //   },
    ],
  },
  resolve: {
    extensions: ['.js', '.jsx'],
  },
  externals:{
    'react': 'React'
  }
};
