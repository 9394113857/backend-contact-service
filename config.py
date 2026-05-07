import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = (
        os.getenv("DATABASE_URL")
        or os.getenv("LOCAL_DB")
    )

    # MAIL
    MAIL_SERVER = os.getenv("MAIL_SERVER")

    MAIL_PORT = int(
        os.getenv("MAIL_PORT", 587)
    )

    MAIL_USE_TLS = (
        os.getenv("MAIL_USE_TLS") == "True"
    )

    MAIL_USERNAME = os.getenv("MAIL_USERNAME")

    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

    SUPPORT_EMAIL = os.getenv("SUPPORT_EMAIL")