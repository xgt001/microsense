#Microsense

A Flask based server infrastructure for supporting Sensors
Note that currently this infra is using JSON, however, after the maturing of the API will move to a suitable database

##Current Supported Platforms:
        Rasbperry Pi

##Implemented Prototype Methods:
    *GET
    *POST

##Backend Technology Stack:
* Flask 
* Sockets.io 
* Flask Sockets
    
##Frontend Technology Stack:
* Semantic-Ui 
* KnockoutJS (yet to)

##API
*Still super early. Early sketch of the API.*

    sid : Sensor ID
    pid : Platform ID
    p_name : Platform Name
    s_name: Sensor Name
    p_desc: Platform description
    s_desc: Sensor description
    s_data: Actual sensor data
    s_live: Boolean value if the data is live or not. In this case need to stream it.

##Current Curl Calls
    +  curl -i -H "Content-Type: application/json" -X POST -d '{jsonhere}' http://127.0.0.1:5000/microsense/api/v0.1/sensors
    +  curl -i http://127.0.0.1:5000/microsense/api/v0.1/sensors
    +  curl -i http://127.0.0.1:5000/microsense/api/v0.1/sensors/sid

##Implemented Platforms at the Moment 
 Raspberry PI UltraSonic Sensor

## ToDO for RBP

 * Data Visualization
 * Template Integration
 * WebSocket Stream to Webapp

## Done for RBP
 * Platform Info
 * Socket Stream to API server
 

##License
>BSD License
