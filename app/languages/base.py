from abc import ABC, abstractmethod
from spacy.language import Language as SpacyModel


class LanguageAnalyzer(ABC):

    @abstractmethod
    def get_language_code(self) -> str:
        """Retorna o código do idioma no formato spaCy/wordfreq: 'en', 'pt', 'es'."""

    @abstractmethod
    def load_model(self) -> SpacyModel:
        """Carrega e retorna o modelo spaCy do idioma."""

    @abstractmethod
    def get_allowed_pos(self) -> set[str]:
        """POS tags relevantes para este idioma (Universal POS do spaCy)."""

    @abstractmethod
    def extract_multi_word_expressions(self, doc, language: str) -> list[dict]:
        """
        Extrai expressões multi-palavra (phrasal verbs, colocações, idioms, etc).

        Args:
            doc:      documento spaCy já processado.
            language: código do idioma no formato wordfreq (ex: 'en', 'pt').

        Returns:
            Lista de dicts com os campos:
              - type          (str)   : 'MULTI_WORD_EXPRESSION' | 'COLLOCATION' | etc.
              - originalText  (str)   : texto exato extraído do documento.
              - lemma         (str)   : forma lematizada da expressão.
              - tokens        (list)  : índices dos tokens no doc.
              - zipfFrequency (float) : frequência Zipf da expressão.
        """