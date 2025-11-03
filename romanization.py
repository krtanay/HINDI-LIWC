"""
Romanization module for Hindi LIWC.

This module currently provides stub functions that simply pass through
input text unchanged.  To properly support Romanized Hindi (written
using Latin script), integrate a transliteration library such as
``indic_transliteration`` or ``Aksharamukha`` here.
"""

def transliterate(text: str) -> str:
    """Transliterate Latin script Hindi into Devanagari.

    Parameters
    ----------
    text : str
        The input text in Latin script.

    Returns
    -------
    str
        The transliterated text.  Currently this is just the input
        unchanged.
    """
    return text