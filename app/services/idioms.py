import spacy
from spacy.matcher import Matcher
from data.idioms_data import patterns

nlp = spacy.load("en_core_web_sm")

matcher = Matcher(nlp.vocab)
matcher.add("IDIOM", patterns)

def extract_idioms(doc):
    results = []

    matches = matcher(doc)

    for match_id, start, end in matches:
        span = doc[start:end]

        results.append({
            "type": "IDIOM",
            "text": span.text,
            "lemma": " ".join([t.lemma_ for t in span]),
            "start": span.start_char,
            "end": span.end_char,
            "tokens": [t.i for t in span]
        })

    return results