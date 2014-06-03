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
* Sockets.io for browser integration
* Flask Sockets
* Python Sockets for Platform to server stream 
    
##Frontend Technology Stack:
* Semantic-Ui GUI framework
* d3.js realtime visualization
* jquery for event binding

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

 * Static Graphs
 * Social Integration Bug Fixes

## Done for RBP
 * Platform Info
 * Socket Stream to API server
 * Template Integration
 * WebSocket Stream to Webapp
 * Live Data Visualization
 

##License
>BSD License

Contrbutor:

Ganesh Hegde

Ashwin Ramanand
