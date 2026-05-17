import spacy
from app.languages.base import LanguageAnalyzer
from .phrasal import extract_phrasal_verbs
from wordfreq import zipf_frequency

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
            frequency = self.expression_frequency(pv.get["lemma"], self.get_language_code.lower())
            results.append({**pv, "type": "MULTI_WORD_EXPRESSION", "zipfFreqeuncy":frequency})
        
        return results
    
    def expression_frequency(expression, language):
        freq = zipf_frequency(expression, language)
        
        if freq > 0:
            return freq
        parts = expression.split()
        values = [
            zipf_frequency(word, language)
            for word in parts
        ]
        return sum(values) / len(values)