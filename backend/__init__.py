from flask import Flask

app = Flask(__name__)

# Import the routes at the bottom to avoid circular imports
from backend import routes
