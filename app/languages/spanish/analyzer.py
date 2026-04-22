import spacy
from app.languages.base import LanguageAnalyzer

class SpanishAnalyzer(LanguageAnalyzer):
    def get_language_code(self): return "ES"
    
    def load_model(self): return spacy.load("es_core_news_sm")
    
    def get_allowed_pos(self): return {"VERB", "NOUN", "ADJ", "ADV"}
    
    def extract_multi_word_expressions(self, doc): ...
