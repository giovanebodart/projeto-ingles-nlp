import spacy
from .phrasal import extract_phrasal_verbs
from .idioms import extract_idioms
from .tokens import extract_tokens 

nlp = spacy.load("en_core_web_sm")


def analyze_text(texts: list[str]):
    results = []
    docs = list(nlp.pipe(texts))  
    for text, doc in zip(texts, docs):
        tokens = extract_tokens(doc)
        expressions = []

        for pv in extract_phrasal_verbs(doc):
            expressions.append({
                "type": "PHRASAL_VERB",
                "text": pv["text"],      
                "lemma": pv.get("lemma"),
                "start": pv.get("start"),
                "end": pv.get("end"),
                "tokens": pv.get("tokens", [])
            })

        for idiom in extract_idioms(doc):
            expressions.append({
                "type": "IDIOM",
                "text": idiom["text"],
                "lemma": idiom.get("lemma"),
                "start": idiom.get("start"),
                "end": idiom.get("end"),
                "tokens": idiom.get("tokens", [])
            })

        expressions.sort(
            key=lambda x: x["start"] if x["start"] is not None else 0
        )

        results.append({
            "text": text,
            "tokens": tokens,
            "expressions": expressions
        })

    return {
        "results": results
    }