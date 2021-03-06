import time
from threading import Thread
from flask import Flask, render_template, session, request
from flask.ext.socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


#def background_thread():
    #"""Example of how to send server generated events to clients."""
    #count = 0
    #while True:
        #time.sleep(10)
        #count += 1
        #socketio.emit('my response',
                      #{'data': 'Server generated event', 'count': count},
                      #namespace='/test')

vay = 4

@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('docLoad')
def test_message(message):
    #session['receive_count'] = session.get('receive_count', 0) + 1
    emit('docReply',"Signal Sent")
    print message
    #emit('my response',
         #{'data': message['data'], 'count': session['receive_count']})


#@socketio.on('connect', namespace='/test')
#def test_connect():
    #emit('my response', {'data': 'Connected', 'count': 0})


#@socketio.on('disconnect', namespace='/test')
#def test_disconnect():
    #print('Client disconnected')


if __name__ == '__main__':
    #Thread(target=background_thread).start()
    socketio.run(app)
