import spacy
from app.languages.base import LanguageAnalyzer
from app.services.nlp.frequency import get_zipf_frequency
from .phrasal import extract_phrasal_verbs


class EnglishAnalyzer(LanguageAnalyzer):

    def get_language_code(self) -> str:
        return "en"

    def load_model(self):
        return spacy.load("en_core_web_sm")

    def get_allowed_pos(self) -> set[str]:
        return {"VERB", "NOUN", "ADJ", "ADV", "PART", "ADP"}

    def extract_multi_word_expressions(self, doc, language: str) -> list[dict]:
        results = []

        for pv in extract_phrasal_verbs(doc):
            lemma = pv.get("lemma", "")
            frequency = get_zipf_frequency(lemma, language)
            results.append({
                **pv,
                "type": "MULTI_WORD_EXPRESSION",
                "zipfFrequency": frequency,
            })

        return results