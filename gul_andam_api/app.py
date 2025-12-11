# gul_andam_api/app.py
"""
Flask app factory for Gul Andam Day 2 API
Run: python -m gul_andam_api.app
"""
from flask import Flask
from .routes import register_routes

def create_app():
    app = Flask(__name__)
    register_routes(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)
