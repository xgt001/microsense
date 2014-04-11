__author__ = 'ganesh'


from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from flask import *
from flask import Flask, render_template
import socket
import time
from flask.ext.socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


# dummy sensor example here 
sensors = [
       {
        'sid': 001,
        'pid': 01,
        'p_name': u'Raspberry Pi',
        's_name': u'Purgatory UV Sensor',
        'p_desc': u'A popular and cost effective SoC',
        's_desc': u'UV Sensor with a range of 150cm',
        's_data': 5,
        's_live': True

    },
    {
        'sid': 002,
        'pid': 02,
        'p_name': u'Raspberry Pi',
        's_name': u'Temperature Sensor',
        'p_desc': u'A popular and cost effective SoC',
        's_desc': u'A Static temperature measurement',
        's_data':0,
        's_live': False

    }
]


server_stream = ''

def socket_launcher():
    s = socket.socket()         # Create a socket object
    host = '192.168.0.103'       # Get local machine name
    port = 4000                # Reserve a port for your service.
    s.connect((host, port))
    while 1:
        streamer = s.recv(1024)
        if not streamer:
            break
        # print streamer
        server_stream = streamer
        time.sleep(3)
    s.close


@app.route('/microsense/api/v0.1/sensors',methods = ['GET'] )
def sensor_fetch_all():
    return jsonify( { 'sensorlog': sensors } )
#
# @app.errorhandler(404)
# def not_found(error):
#     return make_response(jsonify( { 'error': 'No Sensor Entry found' } ), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Invalid Entry!' } ), 400)

@app.route('/microsense/api/v0.1/sensors/<int:s_id>', methods = ['GET'])
def get_sensor(s_id):
    sensor_id = filter(lambda s:s['sid'] == s_id, sensors)
    if len(sensor_id) == 0:
        abort(404)
    return jsonify( { 'sensorlog': sensor_id[0] } )

@app.route('/microsense/api/v0.1/sensors/<int:s_id>', methods = ['PUT'])
def update_sensor(s_id):
    sensor_id = filter(lambda s:s['sid'] == s_id, sensors)
    return "wip"


@app.route('/microsense/api/v0.1/sensors/<int:s_id>', methods = ['DELETE'])
def remove_sensor(s_id):
    sensor = filter(lambda s:s['sid'] == s_id, sensors)
    if len(sensor_id) == 0:
        abort(404)
    sensors.remove(s_id)
    return jsonify( { 'sensorlog': sensors } )

@app.route('/microsense/api/v0.1/sensors', methods = ['POST'])
def create_sensor_entry():
    if not request.json or not 'sid' in request.json:
        abort(400)
    sensor = {
        'sid' : request.json['sid'],
        # 'pid' : request.json['pid'],
        # 'p_name' : request.json['p_name'],
        # 's_name' :request.json['s_name'],
        # 'p_desc' :request.json['p_desc'],
        # 's_desc' :request.json['s_desc'],
        # 's_live' :request.json['s_live'],
        # 's_data' :request.json['s_data']
    }
    sensors.append(sensor)
    return jsonify({'all_sensors':sensors})


#
# @app.route('/socketstream')
# def api():
#     socket_launcher()
#     if request.environ.get('wsgi.websocket'):
#         ws = request.environ['wsgi.websocket']
#     while True:
#         message = ws.wait()
#     ws.send(server_stream)
#     print  server_stream
#     return

# @app.route('/')
# def index():
#     return "Hello World"

# @app.route('/foo/<path:filename>')
# @app.route('/index.html')
# def render_home(filename):
#     return send_from_directory('/template/', filename)




@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect', namespace='/api')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('connectStream')
def start_stream():
    socket_launcher()
    print "stream was started"

@socketio.on('startStream',namespace='/test')
def send_sensor_data(message=server_stream):
    socket_launcher()
    send(message)


@socketio.on('connect', namespace='/test')
def test_connect():
    print "stream connect check"

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app)









#
#
# if __name__ == '__main__':
#     http_server = WSGIServer(('127.0.0.1',5000), app, handler_class=WebSocketHandler)
#     http_server.serve_forever()


# @app.route('/socketstream')
# def stream():
#     socket_launcher()
#     return server_stream
#
# if __name__ == "__main__":
#     app.debug = True
#     app.run()
