module.exports = {
    devServer: {
        disableHostCheck: true,
        devServer: {
            proxy: 'http://localhost:8000'
          }
    }
}