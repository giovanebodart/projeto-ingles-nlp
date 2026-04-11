ALLOWED_POS = {
    "VERB",
    "NOUN",
    "ADJ",
    "ADV",
    "PART",
    "ADP"
}

def extract_tokens(doc):
    tokens = []

    for token in doc:
        if token.pos_ not in ALLOWED_POS:
            continue
        tokens.append({
            "type": "TOKEN",
            "text": token.text,
            "lemma": token.lemma_,
            "pos": token.pos_,
            "start": token.idx,
            "end": token.idx + len(token.text)
        })

    return tokens