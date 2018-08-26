
var Schema={};

Schema.createSchema=function(mongoose){
    TestShcema=mongoose.Schema({
        year:{type:String,required:true,unique:true,'default':''},
        month:{type:String,required:true,unique:true,'default':''},
        day:{type:String,required:true,'default':''},
        sido:{type:String,required:true,'default':''},
        gugun:{type:String,required:true,'default':''},
        PM_avg:{type:Number,required:true,unique:true,'default':''}
    });

    MemberShcema.static('findById',function(id,callback){
        return this.find({"id":id},callback);
    });

    MemberShcema.static('findAll',function(callback){
        return this.find({},callback);
    });

    console.log('TestSchema 정의함');

    return TestShcema;
}

module.exports=Schema;