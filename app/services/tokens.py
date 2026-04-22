def extract_tokens(doc, allowed_pos: set[str]) -> list[dict]:
    tokens = []
    for token in doc:
        if token.pos_ not in allowed_pos:
            continue
        tokens.append({
            "type":  "TOKEN",
            "text":  token.text,
            "lemma": token.lemma_,
            "pos":   token.pos_,
            "start": token.idx,
            "end":   token.idx + len(token.text)
        })
    return tokens