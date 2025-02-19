from flask import Blueprint, request, jsonify
import os
import logging

assets_bp = Blueprint('assets', __name__)

# Directory to store downloadable files
DOWNLOAD_FOLDER = 'path/to/download/folder'

# Configure logging
logger = logging.getLogger(__name__)

@assets_bp.route('/assets', methods=['GET'])
def list_assets():
    """List all downloadable files."""
    try:
        files = os.listdir(DOWNLOAD_FOLDER)
        return jsonify(files), 200
    except Exception as e:
        logger.error("Error listing assets: %s", str(e))
        return jsonify({"error": "Internal server error"}), 500

@assets_bp.route('/assets/<filename>', methods=['GET'])
def download_asset(filename):
    """Download a specific file."""
    try:
        return jsonify({"error": "Not Implemented"}), 501
    except Exception as e:
        logger.error("Error downloading asset %s: %s", filename, str(e))
        return jsonify({"error": "File not found"}), 404
