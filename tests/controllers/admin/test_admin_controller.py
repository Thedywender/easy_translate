from src.models.history_model import HistoryModel
from src.models.user_model import UserModel


def test_history_delete(app_test):
    user = UserModel(
        {"name": "admin", "password": "password", "token": "token"}
    )
    user.save()

    history = HistoryModel({"content": "test content"})
    history.save()

    get_user = UserModel.find_one({"name": "admin"})

    app_test.delete(
        f"/admin/history/{str(history.id)}",
        headers={
            "Authorization": f"Bearer {get_user.data['token']}",
            "User": "admin",
        },
    )
