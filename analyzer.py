"""
Hindi LIWC analyzer
====================

This module provides a simple word‑count–based analyzer inspired by the
Linguistic Inquiry and Word Count (LIWC) framework.  It loads a
dictionary of Hindi words mapped to psycholinguistic categories and
counts category usage in input text.

The implementation is intentionally minimal.  It uses regular
expressions to split tokens, a naive stemmer to handle common Hindi
suffixes, and a placeholder for Romanized transliteration.  For a
production‑quality system you should replace these components with
robust morphological analysis and transliteration libraries.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict, List

# Load resources relative to this file's directory.
BASE_DIR = Path(__file__).resolve().parent
with (BASE_DIR / "categories.json").open(encoding="utf-8") as f:
    CATEGORIES: Dict[str, List[str]] = json.load(f)
with (BASE_DIR / "lexicon.json").open(encoding="utf-8") as f:
    LEXICON: Dict[str, List[str]] = json.load(f)


def transliterate_romanized(text: str) -> str:
    """Return a transliterated version of Romanized Hindi text.

    This placeholder implementation simply returns the text unchanged.
    In practice you would integrate with a library such as
    ``indic_transliteration`` or ``IndicNLP`` to convert Latin script
    to Devanagari.
    """
    return text


def normalize_word(word: str) -> str:
    """Perform a very simple morphological normalization.

    This function lower‑cases the input, strips non‑word characters, and
    removes a handful of common Hindi suffixes.  It is only a rough
    approximation of proper lemmatization.  Replace it with a real
    lemmatizer for better coverage.
    """
    # Keep only letters and numbers from Devanagari or Latin scripts.
    word = re.sub(r"[^\w\u0900-\u097F]", "", word.lower())
    # Remove common suffixes (plural and case markers).  This list is
    # non‑exhaustive but illustrates the approach.
    suffixes = [
        "याँ", "ें", "ों", "ाएं", "ियाँ", "ियाँ", "ीयाँ", "यी", "ी", "ा", "े", "ो", "ता", "ते",
        "ती", "ना", "ने", "ने", "ने", "ने"
    ]
    for suffix in suffixes:
        if word.endswith(suffix) and len(word) > len(suffix) + 1:
            return word[: -len(suffix)]
    return word


def analyze(text: str) -> Dict[str, int]:
    """Analyze input text and return category counts.

    The analysis proceeds as follows:

    1. Transliterates Romanized Hindi to Devanagari (placeholder).
    2. Tokenizes the text into word tokens using a regular expression.
    3. Normalizes each token using ``normalize_word``.
    4. Looks up each normalized token in the lexicon and increments
       category counts accordingly.

    Parameters
    ----------
    text : str
        The raw text to analyze.

    Returns
    -------
    Dict[str, int]
        A mapping from category names to their counts in the text.
    """
    # Convert Romanized input.  This implementation currently does nothing.
    text = transliterate_romanized(text)
    # Extract word tokens (Devanagari letters, Latin letters, digits).
    tokens = re.findall(r"[\w\u0900-\u097F]+", text)
    counts: Dict[str, int] = {}
    for token in tokens:
        base = normalize_word(token)
        if not base:
            continue
        categories = LEXICON.get(base)
        if categories is None:
            continue
        # Update counts for each category (including hierarchical names)
        for category in categories:
            counts[category] = counts.get(category, 0) + 1
    return counts


def main() -> None:
    """Simple command‑line interface for testing.

    Run this module directly to analyze text entered on stdin.  Usage:

        python -m liwc_hindi.analyzer

    The script will read lines from standard input and print category
    counts for each input.
    """
    import sys

    print("Enter Hindi text (Ctrl‑D to end):")
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        result = analyze(line)
        print(result)


if __name__ == "__main__":
    main()