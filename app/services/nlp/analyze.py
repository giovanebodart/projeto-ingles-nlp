from app.services.nlp.registry import resolve
from app.services.nlp.tokens import extract_tokens

def analyze_text(url: str, texts: list[str], language: str) -> dict:
    analyzer, nlp = resolve(language)

    results = []
    docs = list(nlp.pipe(texts))

    for text, doc in zip(texts, docs):
        tokens      = extract_tokens(doc, analyzer.get_allowed_pos(), language)
        expressions = analyzer.extract_multi_word_expressions(doc, language)

        expressions.sort(key=lambda x: x.get("start") or 0)

        results.append({
            "text":        text,
            "tokens":      tokens,
            "expressions": expressions
        })

    return {"url": url, "language": analyzer.get_language_code().upper(), "results": results}