from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Configurações podem ser carregadas aqui
    app.config.from_pyfile('config.py', silent=True)
    
    from app.routes import meteogram_bp
    app.register_blueprint(meteogram_bp)
    
    return app
