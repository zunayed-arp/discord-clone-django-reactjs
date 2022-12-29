module.exports = {
    module:{
        rules:[
            {
                test:/\.js$/,
                exclude:/node_modules/,
                user:{
                    loader:"babel-loader"
                }
            }
        ]
    }
};