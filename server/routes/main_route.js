module.exports=function(router){
    router.all('/',function(req,res){
        res.redirect('/index');
    });
    
    router.all('/index',function(req,res){
        console.log('index 실행')
        res.render('index');
    });

    router.all('/chatbot',function(req,res){
        console.log('chatbot 실행')
        res.render('chatbot');
    });

    router.all('/predust',function(req,res){
        console.log('predust 실행')
        res.render('predust');
    });
    router.all('/folium',function(req,res){
        console.log('folium 실행')
        res.render('folium');
    });

}