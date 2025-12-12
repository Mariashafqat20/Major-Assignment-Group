# gul_andam_api/app.py
"""
Flask app factory for Gul Andam API (Day 2/3/4)
Run: python -m gul_andam_api.app
"""
from flask import Flask
from flask_cors import CORS

from .routes import register_routes
from .report_routes import report_api

def create_app():
    app = Flask(__name__)
    CORS(app)  # allow browser access during local dev
    register_routes(app)
    app.register_blueprint(report_api, url_prefix="/report")
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="127.0.0.1", port=5001)
