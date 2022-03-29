from deep_translator.base import BaseTranslator


def get_translation(t: BaseTranslator, text: str, **kwargs):
    try:
        resp = t.translate(text, **kwargs)
        return {"translation": resp}
    except Exception as ex:
        return {"error": str(ex)}


def get_summary(translator: str):
    return f"Translate text using the {translator} translator"
