var database;
var MemberSchema;
var MemberModel;

var init=function(db,schema,model){
    database=db;
    MemberSchema=schema;
    MemberModel=model;
}

var login=function(req,res){
    console.log('user 모듈 안에 있는 login 호출됨');

    var paramId=req.body.id||req.query.id;
    var paramPassword=req.body.password||req.query.password;

    if(database){
        authUser(database,paramId,paramPassword,function(err,docs){
            if(err) throw err;

            if(docs){
                console.dir(docs);

                var membername=docs[0].name;

                res.writeHead('200',{'Content-Type':'text/html;charset=utf8'});
                res.write('<h1>로그인 성공</h1>');
                res.write('<div><p> 아이디 : '+paramId+'</p></div>');
                res.write('<div><p> 사용자 이름 : '+membername+'</p></div><br>');
                res.write("<a href='/public/login.html'>다시 로그인</a>");
                res.write("<a href='/public/search.html'>약품 검색 페이지</a>");
                res.end();
            }else{
                res.writeHead('200',{'Content-Type':'text/html;charset=utf8'});
                res.write('<h1>로그인 실패</h1>');
                res.write("<a href='/public/login.html'>다시 로그인</a>");
                res.end();
            }
        });
    }else{
        res.writeHead('200',{'Content-Type':'text/html;charset=utf8'});
        res.write('<h1>데이터베이스를 찾을 수 없습니다.</h1>');
        res.end();
    }
}

var listuser=function(req,res){
    console.log('user 모듈 안에 있는 listuser 호출됨');

    if(database){
        MemberModel.findAll(function(err,results){
            if(err){
                console.log('오류 발생');
                res.writeHead('200',{'Content-Type':'text/html;charset=utf8'});
                res.write('<h2>조회 중 오류 발생');
                res.end();
                return;
            }
            if(results){
                console.dir(results);

                res.writeHead('200',{'Content-Type':'text/html;charset="utf-8'});
                res.write('<h2>사용자 리스트</h2>');
                res.write('<div><ul>');
                for(var i=0;i<results.length;i++){
                    var curId=results[i]._doc.id;
                    var curName=results[i]._doc.name;
                    res.write('<li>#'+i+' : '+curId+', '+curName);
                }
                res.write('</ul></div>');
                res.end();
            }
        });
    }else{
        res.writeHead('200',{'Content-Type':'text/html;charset="utf-8'});
        res.write('<h2>데이터 베이스 연결 실패!!</h2>');
        res.end();
    }
}

var adduser=function(req,res){
    console.log('user 모듈 안에 있는 adduser 호출됨');

    var paramId=req.body.id;
    var paramPassword=req.body.password;
    var paramName=req.body.name;
    var gender=req.body.gender;
    var location=req.body.location;
    var phone=req.body.phoneNumber;


    if(database){
        addUser(database,paramId,paramPassword,paramName,gender,location,phone,function(err,result){
            if(err) throw err;

            if(result){
                console.dir(result);
                console.log(gender+" "+location+" "+phone);

                res.writeHead('200',{'Content-Type':'text/html;charset=utf8'});
                res.write('<h2>사용자 추가 완료</h2>');
                res.write("<a href='/public/login.html'>다시 로그인</a>");
                res.write("<a href='/public/adduser.html'>사용자 추가</a>");
                res.end();
            }else{
                res.writeHead('200',{'Content-Type':'text/html;charset=utf8'});
                res.write('<h2>사용자 추가 실패</h2>');
                res.write("<a href='/public/login.html'>다시 로그인</a>");
                res.write("<a href='/public/adduser.html'>사용자 추가</a>");
                res.end();
            }

        });
    }else{
        res.writeHead('200',{'Content-Type':'text/html;charset=utf8'});
        res.write('<h2>데이터베이스 연결 실패</h2>');
        res.end();
    }
}

var authUser=function(database,id,password,callback){
    console.log('authUser 호출됨');

    MemberModel.findById(id,function(err,result){
        if(err){
            callback(err,null);
            return;
        }
        console.log('아이디 [%s]로 사용자 검색',id);
        console.dir(result);

        if(result.length>0){
            console.log('일치하는 사용자 찾음');

            var user=new MemberModel({"id":id});
            var authenticated=user.authenticate(password,result[0]._doc.salt,result[0]._doc.hashed_password);

            if(authenticated){
                console.log('비밀번호 일치함');
                callback(null,result);
            }else{
                console.log('일치하지 않음');
                callback(null,null);
            }
        }else{
            console.log('일치하는 사용자 없음');
            callback(null,null);
        }
    });
}

var addUser=function(database,id,password,name,gender,location,phone,callback){
    console.log('addUser 호출됨');

    var user=new MemberModel({"id":id,"password":password,"name":name,"gender":gender,"location":location,"phoneNumber":phone});

    user.save(function(err){
        if(err){
            callback(err,null);
        }
        console.log('사용자 데이터 추가');
        callback(null,user);
    });
}
module.exports.init=init
module.exports.login=login;
module.exports.listuser=listuser;
module.exports.adduser=adduser;

