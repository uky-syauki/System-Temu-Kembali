from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'  # Ubah dengan secret key kamu
socketio = SocketIO(app)

from app import routes, stk