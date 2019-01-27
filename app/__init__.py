from flask import Flask
from flask_socketio import SocketIO
socketio = SocketIO()

def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['UPLOAD_FOLDER'] = '/uploads'
    app.secret_key = 'pbkdf2:sha256:50000$IyKvTYMl$0c5f1409ca4c6353ed8c28ff5aa8955331c4ac4c990e967a9520ea474ae5ecc0'
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    socketio.init_app(app)
    return app
