def extract_phrasal_verbs(doc):
    results = []
    for token in doc:
        if token.pos_ != "VERB":
            continue
        for child in token.children:
            if child.dep_ == "prt":
                start = min(token.i, child.i)
                end = max(token.i, child.i) + 1

                span = doc[start:end]

                results.append({
                    "type": "PHRASAL_VERB",
                    "text": span.text,
                    "lemma": f"{token.lemma_} {child.lemma_}",
                    "start": span.start_char,
                    "end": span.end_char,
                    "tokens": [t.i for t in span]
                })

    return results