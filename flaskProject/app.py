from flask import Flask,render_template
import time
import sys
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def session():
    return render_template('index.html')

def ellapsedtime(number_of_popups = 4, repeat_popup = 20,methods = ['POST']):
    start_time = time.time()
    for i in range(number_of_popups):
        # socketio.sleep(0)
        while(True):
            socketio.sleep(0)
            if (int(time.time() - start_time) == int(repeat_popup)):
        # time.sleep(repeat_popup)
                print(" ------sending data ------    ")
                j = i+1
                obj = "Pop up" + str(j)
                emit("flask event", obj)
                start_time = time.time()
                break
            else:
                emit("empty event", {})
                continue
    print("out of all the loops !!")



@socketio.on('foo')
def handle_event(data, methods = ['GET']):
    socketio.sleep(0)
    ellapsedtime(number_of_popups=data['number_of_popups'],
                 repeat_popup=data['repeat_popup'])

if __name__ == '__main__':
    socketio.run(app, debug=True)


