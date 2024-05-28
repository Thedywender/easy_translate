from flask import Blueprint, jsonify
from models.history_model import HistoryModel

history = Blueprint("history", __name__)


@history.get("/")
def get_history():
    history_list = HistoryModel.list_as_json()
    if not history_list:
        return jsonify({"error": "No history found"}), 404
    return history_list, 200
