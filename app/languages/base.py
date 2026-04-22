from abc import ABC, abstractmethod
from spacy.language import Language as SpacyModel

class LanguageAnalyzer(ABC):

    @abstractmethod
    def get_language_code(self) -> str:
        """Retorna o código do idioma: 'EN', 'PT', 'ES'"""

    @abstractmethod
    def load_model(self) -> SpacyModel:
        """Carrega e retorna o modelo spaCy do idioma"""

    @abstractmethod
    def extract_multi_word_expressions(self, doc) -> list[dict]:
        """
        Extrai expressões multi-palavra (phrasal verbs, colocações, idioms, etc).
        Retorna sempre o tipo universal MULTI_WORD_EXPRESSION ou COLLOCATION.
        """

    @abstractmethod
    def get_allowed_pos(self) -> set[str]:
        """POS tags relevantes para este idioma (usando Universal POS do spaCy)"""