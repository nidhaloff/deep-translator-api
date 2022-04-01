from deep_translator.base import BaseTranslator


def get_translation(t: BaseTranslator, text: str, **kwargs):
    """Get a translation response using a specific translator"""
    try:
        resp = t.translate(text, **kwargs)
        return {"translation": resp}
    except Exception as ex:
        return {"error": str(ex)}


def get_summary(translator: str):
    """return a string representing a summary to document the api"""
    return f"Translate text using the {translator} translator"
