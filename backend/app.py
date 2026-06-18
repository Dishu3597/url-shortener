from flask import Flask
from flask_cors import CORS

from config import Config
from models import db
from models.url import URL

from routes.url_routes import url_bp
app = Flask(__name__)
CORS(
    app,
    resources={
        r"/*": {
            "origins": [
                "http://localhost:5173",
                "https://url-shortener-1-f3ke.onrender.com"
            ]
        }
    }
)

app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(url_bp)


@app.route("/")
def home():
    return {
        "message": "URL Shortener API is running!"
    }


if __name__ == "__main__":
    app.run(debug=True)