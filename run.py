from flask import Flask
from app.app import upload_blueprint
import config

# Flask Configurações
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = config.UPLOAD_FOLDER

# Register blueprints
app.register_blueprint(upload_blueprint) # Home

if __name__ == '__main__':
    app.run()
