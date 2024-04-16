from typing import Dict, List
from database.db import db
from models.abstract_model import AbstractModel


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data: Dict[str, str]):
        super().__init__(data)

    def to_dict(self) -> Dict[str, str]:
        return {"name": self.data["name"], "acronym": self.data["acronym"]}

    @classmethod
    def list_dicts(cls) -> List[Dict[str, str]]:
        languages = cls._collection.find()
        return [cls(language).to_dict() for language in languages]
