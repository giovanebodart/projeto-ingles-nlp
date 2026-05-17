from wordfreq import zipf_frequency

def get_frequency(lemma: str, language: str) -> float:
    try:
        return zipf_frequency(lemma, language)
    except:
        return 0.0

def extract_tokens(doc, allowed_pos: set[str], language: str) -> list[dict]:
    tokens = []
    for token in doc:
        if token.pos_ not in allowed_pos:
            continue
        lemma = token.lemma_.lower()
        frequency = get_frequency(lemma, language)
        tokens.append({
            "type":  "TOKEN",
            "originalText":  token.text,
            "lemma": token.lemma_,
            "zipfFrequency": frequency, 
            "pos":   token.pos_
        })
    return tokens