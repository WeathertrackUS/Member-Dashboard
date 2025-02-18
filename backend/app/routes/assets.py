from flask import Blueprint, request, jsonify
import os

assets_bp = Blueprint('assets', __name__)

# Directory to store downloadable files
DOWNLOAD_FOLDER = 'path/to/download/folder'

@assets_bp.route('/assets', methods=['GET'])
def list_assets():
    """List all downloadable files."""
    try:
        files = os.listdir(DOWNLOAD_FOLDER)
        return jsonify(files), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@assets_bp.route('/assets/<filename>', methods=['GET'])
def download_asset(filename):
    """Download a specific file."""
    try:
        return jsonify({"error": "Not Implemented"}), 501  
        # return send_from_directory(DOWNLOAD_FOLDER, filename, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 404