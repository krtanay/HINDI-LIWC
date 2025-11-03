"""
Placeholder for Hindi morphological processing.

In the full LIWC pipeline this module would implement proper
tokenization, stemming or lemmatization, and handling of inflections in
Hindi.  The current implementation merely wraps the function in
``analyzer.normalize_word``.  You can extend this module to integrate
with the Indic NLP Library, iNLTK, or any other morphological
analyzer.
"""

from typing import Iterable

from .analyzer import normalize_word


def normalize_tokens(tokens: Iterable[str]) -> Iterable[str]:
    """Normalize a sequence of tokens.

    Parameters
    ----------
    tokens : Iterable[str]
        Raw tokens (words) to normalize.

    Yields
    ------
    str
        Normalized base forms of the tokens.
    """
    for token in tokens:
        base = normalize_word(token)
        if base:
            yield base