from wordfreq import zipf_frequency

def get_zipf_frequency(expression: str, language: str) -> float:
    """
    Retorna a frequência Zipf de uma expressão em determinado idioma.

    Para expressões multi-palavra, tenta primeiro obter a frequência
    da expressão completa. Se não encontrada (freq == 0), retorna a
    média das frequências de cada palavra individualmente.

    Args:
        expression: palavra ou expressão a ser consultada.
        language:   código de idioma no formato wordfreq (ex: 'en', 'pt', 'es').

    Returns:
        Valor Zipf (float). Quanto maior, mais frequente.
    """
    try:
        freq = zipf_frequency(expression, language)
        if freq > 0:
            return freq

        parts = expression.split()
        if len(parts) <= 1:
            return 0.0

        part_freqs = [zipf_frequency(word, language) for word in parts]
        return sum(part_freqs) / len(part_freqs)
    except Exception:
        return 0.0