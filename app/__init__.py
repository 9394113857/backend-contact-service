from flask import Flask
from flask_cors import CORS

from config import Config
from extensions import db, migrate, mail

from app.routes.contact_routes import contact_bp

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    # =========================
    # INIT EXTENSIONS
    # =========================
    db.init_app(app)

    migrate.init_app(app, db)

    mail.init_app(app)

    # =========================
    # CORS
    # =========================
    CORS(app)

    # =========================
    # REGISTER ROUTES
    # =========================
    app.register_blueprint(contact_bp)

    return app