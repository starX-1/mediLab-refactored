from flask import Blueprint, request, jsonify
from controllers.imageControllers import save_image

image_blueprint = Blueprint('image', __name__, url_prefix='/image')

@image_blueprint.route('/upload', methods=['POST'])
def upload():
    if "image" not in request.files:
        return jsonify({"message": "No file uploaded"}), 400

    file = request.files["image"]
    filepath = save_image(file)
    if filepath:
        return jsonify({"message": "File uploaded successfully", "filepath": filepath}), 200
    else:
        return jsonify({"error": "Failed to upload image"}), 400