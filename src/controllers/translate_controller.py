from flask import Blueprint, render_template

from src.models.language_model import LanguageModel

language = Blueprint("language", __name__)


@language.get("/")
def render_language_page():
    languages = LanguageModel.list_dicts()
    text_translate = "O que deseja traduzir?"
    translate_from = "pt"
    translate_to = "en"
    translated = "What do you want to translate?"
    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )
