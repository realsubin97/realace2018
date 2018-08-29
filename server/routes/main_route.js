

module.exports=function(router){

    router.all('/',function(req,res){
        res.redirect('/main');
    });

    router.all('/main',function(req,res){
        console.log('main 실행')
        res.render('main');
    });

    router.all('/index',function(req,res){
        console.log('index 실행')
        res.render('index');
    });

    router.all('/folium',function(req,res){
        console.log('folium 실행')
        res.render('folium');
    });


    router.route('/process/withdraw').post(function(req,res){
        console.log('/process/withdraw 호출됨');

        var userId=req.body.id;
        var userPass=req.body.password;

        checkUser(userId,userPass,function(err,result){
            if(err){
                console.error("사용자 삭제 중 에러 발생"+err.stack);

                res.writeHeader('400',{'Content-Type':'text/html;charset=utf-8'});
                res.write('<h2>사용자 삭제 중 에러 발생</h2>');
                res.write('<p>'+err.stack+'</p>');
                res.end();
                return;
            }else if(result){
                delUser(userId,function(err,result){
                    if(err){
                        console.log('탈퇴 실패');
                    }else{
                        console.log('탈퇴 완료');
                    }
                })
                res.send("<script>alert('탈퇴가 완료 되었습니다.');location.href='/logout'</script>");
                console.log('유저 삭제 완료');
            }
        });
    });

    router.route('/process/modify').post(function(req,res){
        console.log('/process/modify 호출됨');

        var id=req.body.id;
        var pass=req.body.password;
        var name=req.body.name;
        var age=req.body.age;
        var gender=req.body.gender;

        modifyUser(id,pass,name,age,gender,function(err,result){
            if(err){
                console.error("사용자 수정 중 에러 발생"+err.stack);

                res.writeHeader('400',{'Content-Type':'text/html;charset=utf-8'});
                res.write('<h2>사용자 수정 중 에러 발생</h2>');
                res.write('<p>'+err.stack+'</p>');
                res.end();
                return;
            }else if(result){
                res.send("<script>alert('회원 수정이 완료 되었습니다.');location.href='/logout'</script>");
                console.log('회원 수정 완료');
            }
        });
    });

    function addUser(id,pass,name,age,gender,callback){
        console.log('addUser 호출됨');

        db.get().query(sql.insertMem,[id,pass,name,age,gender],function(err,result){
            if(err){
                console.log('사용자 추가 중 에러 발생');
                callback(err,null);
                return;
            }else{
                console.log('사용자 추가 완료');
                callback(null,result);
            }
        });
    }

    function addRank(id,callback){
        console.log('addRank 호출됨');

        db.get().query(sql.insertRank,id,function(err,result){
            var user=result[0];

            if(err){
                callback(err,null);
            }else{
                callback(null,result);
            }
        });
    }

    function checkUser(id,password,callback){
        console.log('checkUser 호출됨');

        db.get().query(sql.checkIdPass,[id],function(err,result){
            var user=result[0];
            if(err){
                console.log('사용자 조회중 에러발생');
                callback(err,null);
                return;
            }
            else if(!user){
                console.log('입력하신 아이디는 없는 아이디 입니다.');
                callback(null,req.flash('failure','입력하신 아이디는 없는 아이디 입니다.'));
                return;
            }
            else if(user.user_pass != password){   
                console.log('비밀번호가 틀립니다.');
                callback(null,req.flash('failure','비밀번호가 틀립니다.'));
                return;
            }else{
                callback(null,user);
                return;
            }
        })
    }

    function delUser(id,callback){
        console.log('delUser 호출됨');

        db.get().query(sql.deleteMem,id,function(err,result){
            if(err){
                callback(err,null);
                return;
            }
            else{
                callback(null,result);
                return;
            }
        })
    }

    function modifyUser(id,pass,name,age,sex,callback){
        console.log('modifyUser 호출됨');

        db.get().query(sql.modifyMem,[pass,name,age,sex,id],function(err,result){
            if(err){
                callback(err,null);
                return;
            } else{
                callback(null,result)
                return;
            }
        })
    }

    router.all("/checkId",function(req,res){
        var checked;

        var id=req.body.id;
        db.get().query(sql.selectId,id,function(err,result){
            if(err)
                throw err;
            if(result[0].cnt==1)
                checked="NO";
            
            else
                checked="YES";        
            res.send({result:checked});
        })
    })
}