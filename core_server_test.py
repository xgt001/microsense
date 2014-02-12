__author__ = 'ganesh'

from flask import *
app = Flask(__name__)


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
#
@app.route('/microsense/api/v0.1/sensors',methods = ['GET'] )
def sensor_fetch_all():
    return jsonify( { 'sensorlog': sensors } )

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'No Sensor Entry found' } ), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Invalid Entry!' } ), 400)


@app.route('/microsense/api/v0.1/sensors/<int:s_id>', methods = ['GET'])
def get_sensor(s_id):
    sensor_id = filter(lambda s:s['sid'] == s_id, sensors)
    if len(sensor_id) == 0:
        abort(404)
    return jsonify( { 'sensorlog': sensor_id[0] } )

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


@app.route('/')
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.debug = True
    app.run()
