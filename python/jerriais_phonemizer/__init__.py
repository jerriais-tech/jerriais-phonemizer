"""Jèrriais to IPA phonemizer.

The rules live in src/*.sbl; _snowball/ is generated from them by `make python`.
"""

from jerriais_phonemizer._snowball.phonemizer import Phonemizer

__all__ = ["phonemize"]


def phonemize(text: str, separator: str = "") -> str:
    """Return the IPA for lowercase Jèrriais `text`, words separated by spaces.

    Uppercase letters and punctuation are dropped. With `separator`, it goes
    between the phones of each word ("b|w|õː|ʒ|u|r").
    """
    # A fresh Snowball object per call: it holds the separator and the text as state.
    p = Phonemizer()
    p.set_current(separator)
    p.set_separator()
    p.set_current(text)
    p.phonemize()
    return p.get_current()
