import spacy
from app.languages.base import LanguageAnalyzer
from .phrasal import extract_phrasal_verbs

_TYPE_MAP = {
    "PHRASAL_VERB": "MULTI_WORD_EXPRESSION",
    "IDIOM":        "COLLOCATION",
    "TOKEN":        "TOKEN"
}
class EnglishAnalyzer(LanguageAnalyzer):

    def get_language_code(self) -> str:
        return "EN"

    def load_model(self):
        return spacy.load("en_core_web_sm")

    def get_allowed_pos(self) -> set[str]:
        return {"VERB", "NOUN", "ADJ", "ADV", "PART", "ADP"}

    def extract_multi_word_expressions(self, doc) -> list[dict]:
        results = []

        for pv in extract_phrasal_verbs(doc):
            results.append({**pv, "type": _TYPE_MAP["PHRASAL_VERB"]})
        
        return results