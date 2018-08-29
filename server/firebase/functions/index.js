'use strict';

const functions = require('firebase-functions');
const date=require("date-utils");
const moment=require('moment-timezone');

const {WebhookClient}=require('dialogflow-fulfillment');


const admin = require('firebase-admin');
admin.initializeApp(functions.config().firebase);

const DialogflowApp = require('actions-on-google').DialogflowApp;


exports.pmFunction = functions.https.onRequest((request, response) => {
    const agent=new WebhookClient({request,response});

    function startApp(agent){
        const name=request.body.queryResult.parameters.Myname;

        if(name&&name.length>0){
            agent.add("불렀냐?ㅋㅋㅋzz??");
        }
    }

    function weatherApp(agent){
        const location=request.body.queryResult.parameters.location;
        const weather=request.body.queryResult.parameters.weather;
        const sidoName=request.body.queryResult.parameters.sidoName;
        const cityname=request.body.queryResult.parameters.cityname;

        //const dbLocation=admin.database().ref('/pm').once('value');
        const key=admin.database().ref('/pm').push().key;
        const dbLocation=admin.database().ref('/pm').once('value');

        var sidoF=false;
        var cityF=false;
        var succ=false;

        var d = moment().tz('Asia/Seoul').format('YYYY-MM-DD 02:00');
        return dbLocation.then((data)=>{
            data.forEach(function(snapshot){
                const key=snapshot.key;
                const valu=snapshot.val();
                var dataValue=null;
                var dt = new Date(date.now);

                if(weather&&weather.length>0){
                    if((sidoName&&sidoName.length>0)&&valu.sidoname==sidoName){
                        if(((cityname&&cityname.length>0)&&valu.cityname==cityname)&&d==valu.datatime){
                            if(!succ){
                                agent.add("현재"+valu.sidoname+" "+valu.cityname+"의 미세먼지는 "+valu.pm10vale);                           
                                succ=true;
                            }
                        }else{
                            cityF=true;
                        }          
                    }else{
                            sidoF=true;
                    }
                }
            });
            if(!succ){
                if(sidoF){
                    agent.add("도시명을 알려주세요ㅠㅠ");
                }
                if(cityF){
                    agent.add("자세한 지역명을 알려주세요ㅠㅠ");
                }
            }         
            
        });
    }  

    let intentMap=new Map();

    intentMap.set("StartAppIntent",startApp);
    intentMap.set("WeatherAppIntent",weatherApp);

    agent.handleRequest(intentMap);
});

