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



config = {"development": DevelopmentConfig,
          "production": ProductionConfig}

