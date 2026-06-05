from app.services.nlp.frequency import get_zipf_frequency


def extract_tokens(doc, allowed_pos: set[str], language: str) -> list[dict]:
    """
    Extrai tokens relevantes do documento spaCy.

    Filtra por POS tags permitidas e enriquece cada token
    com sua frequência Zipf no idioma informado.

    Args:
        doc:         documento spaCy processado.
        allowed_pos: conjunto de POS tags a incluir.
        language:    código do idioma no formato wordfreq (ex: 'en', 'pt').

    Returns:
        Lista de dicts com os campos:
          - type          (str)   : sempre 'TOKEN'.
          - originalText  (str)   : texto exato do token no documento.
          - lemma         (str)   : forma lematizada do token.
          - pos           (str)   : POS tag Universal.
          - zipfFrequency (float) : frequência Zipf do lema.
    """
    tokens = []

    for token in doc:
        if token.pos_ not in allowed_pos:
            continue

        lemma = token.lemma_.lower()
        tokens.append({
            "type":          "TOKEN",
            "originalText":  token.text,
            "lemma":         token.lemma_,
            "pos":           token.pos_,
            "zipfFrequency": get_zipf_frequency(lemma, language),
        })

    return tokens