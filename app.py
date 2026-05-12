from flask import Flask
from config import Config
from models.producto import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from controllers.producto_controller import producto_bp
    app.register_blueprint(producto_bp)

    with app.app_context():
        db.create_all() 

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug = True) 