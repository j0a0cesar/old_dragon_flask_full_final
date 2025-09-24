from flask import Flask
from controllers.character_controller import bp as character_bp


def create_app():
    app = Flask(__name__)
    app.secret_key = 'dev-secret-key'
    app.register_blueprint(character_bp)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')
