from app.languages.base import LanguageAnalyzer
from app.languages.english.analyzer import EnglishAnalyzer
from app.languages.spanish.analyzer import SpanishAnalyzer

_REGISTRY: dict[str, LanguageAnalyzer] = {
    "EN": EnglishAnalyzer(),
    "ES": SpanishAnalyzer()
}

_MODEL_CACHE: dict[str, object] = {}

def resolve(language_code: str) -> tuple[LanguageAnalyzer, object]:
    code = language_code.upper()

    if code not in _REGISTRY:
        supported = list(_REGISTRY.keys())
        raise ValueError(f"Idioma '{code}' não suportado. Suportados: {supported}")

    analyzer = _REGISTRY[code]

    if code not in _MODEL_CACHE:
        _MODEL_CACHE[code] = analyzer.load_model()

    return analyzer, _MODEL_CACHE[code]