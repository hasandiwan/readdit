import os


class Config:
    """Configuration settings for the Flaskeddit Flask app."""

    SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(16))
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
