# Main code document for SQLAlchemy Homework

# Import Flask
from flask import Flask

# Set up app
app = Flask(__name__)

# Establish necessary framework for webpage
# Define static route
@app.route("/")
def index():
    return "SQLAlchemy Homework"















# Base needed code
if __name__ == "__main__":
    app.run(debug=True)