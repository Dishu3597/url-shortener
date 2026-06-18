from flask import Blueprint, request, jsonify, redirect

from models import db
from models.url import URL
from services.shortener import generate_short_code
from utils.validators import is_valid_url

url_bp = Blueprint("url_bp", __name__)


@url_bp.route("/shorten", methods=["POST"])
def shorten_url():

    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    original_url = data.get("url")

    if not original_url:
        return jsonify({"error": "URL is required"}), 400

    if not is_valid_url(original_url):
        return jsonify({"error": "Invalid URL"}), 400

    short_code = generate_short_code()

    # Ensure the generated short code is unique
    while URL.query.filter_by(short_code=short_code).first():
        short_code = generate_short_code()

    new_url = URL(
        original_url=original_url,
        short_code=short_code
    )

    db.session.add(new_url)
    db.session.commit()

    return jsonify({
    "shortCode": short_code,
    "shortUrl": f"{request.host_url.rstrip('/')}/{short_code}"
    }), 201


@url_bp.route("/<string:short_code>", methods=["GET"])
def redirect_url(short_code):

    url = URL.query.filter_by(short_code=short_code).first()

    if not url:
        return jsonify({"error": "Short URL not found"}), 404

    # Increment visit count
    url.visit_count += 1
    db.session.commit()

    # Redirect to the original URL
    return redirect(url.original_url)

@url_bp.route("/analytics/<string:short_code>", methods=["GET"])
def get_analytics(short_code):


    url = URL.query.filter_by(short_code=short_code).first()

    if not url:
        return jsonify({"error": "Short URL not found"}), 404

    return jsonify({
        "originalUrl": url.original_url,
        "shortCode": url.short_code,
        "visitCount": url.visit_count,
        "createdAt": url.created_at.isoformat()
    }), 200