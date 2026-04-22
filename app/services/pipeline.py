from app.services.registry import resolve
from app.services.tokens import extract_tokens

def analyze_text(texts: list[str], language: str) -> dict:
    analyzer, nlp = resolve(language)

    results = []
    docs = list(nlp.pipe(texts))

    for text, doc in zip(texts, docs):
        tokens      = extract_tokens(doc, analyzer.get_allowed_pos())
        expressions = analyzer.extract_multi_word_expressions(doc)

        expressions.sort(key=lambda x: x.get("start") or 0)

        results.append({
            "text":        text,
            "language":    analyzer.get_language_code(),
            "tokens":      tokens,
            "expressions": expressions
        })

    return {"results": results}