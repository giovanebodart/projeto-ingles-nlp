"""Idioms patterns used by the spaCy matcher."""

# Each entry is a spaCy matcher token pattern.
patterns = [
    [{"LOWER": "break"}, {"LOWER": "a"}, {"LOWER": "leg"}],
    [{"LOWER": "piece"}, {"LOWER": "of"}, {"LOWER": "cake"}],
    [{"LOWER": "hit"}, {"LOWER": "the"}, {"LOWER": "sack"}],
    [{"LOWER": "once"}, {"LOWER": "in"}, {"LOWER": "a"}, {"LOWER": "blue"}, {"LOWER": "moon"}],
    [{"LOWER": "under"}, {"LOWER": "the"}, {"LOWER": "weather"}],
]
