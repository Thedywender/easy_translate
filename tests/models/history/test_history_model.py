import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    history_json = HistoryModel.list_as_json()
    history_data = json.loads(history_json)

    base_data = [
        {
            "text_to_translate": "Hello, I like videogame",
            "translate_from": "en",
            "translate_to": "pt",
        },
        {
            "text_to_translate": "Do you love music?",
            "translate_from": "en",
            "translate_to": "pt",
        },
    ]

    for data in history_data:
        del data["_id"]

    for data in base_data:
        assert data in history_data
