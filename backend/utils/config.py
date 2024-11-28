import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    "Base Configuration"

class DevelopmentConfig:

    "Development Configuration"

    DEBUG = True
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
    MONGO_DB_USERNAME = os.getenv("MONGO_DB_USERNAME")
    MONGO_DB_PASSWORD = os.getenv("MONGO_DB_PASSWORD")
    REDIS_ENDPOINT = os.getenv("REDIS_ENDPOINT")
    REDIS_PORT = os.getenv("REDIS_PORT")
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")


class ProductionConfig:

    "Production Configuration"

    DEBUG = True
    MONGO_URI = os.environ.get("MODEL_URI")
    REDIS_ENDPOINT = os.environ.get("REDIS_ENDPOINT")

    redis_host = os.environ.get("REDIS_HOST")
    redis_port = os.environ.get("REDIS_PORT")
    postgres_host = os.environ.get("POSTGRES_HOST")
    postgress_username = os.environ.get("POSTGRES_USERNAME")
    postgress_password = os.environ.get("POSTGRES_PASSWORD")



config = {"development": DevelopmentConfig,
          "production": ProductionConfig}

