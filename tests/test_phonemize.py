import csv
from pathlib import Path

import pytest

from jerriais_phonemizer import phonemize

TESTS = Path(__file__).parent


def read_cases():
    with open(TESTS / "test_cases.csv", newline="", encoding="utf-8") as f:
        return [(row["input"], row["expected_output"]) for row in csv.DictReader(f)]


def mismatches(pairs):
    return [(text, expected, actual) for text, expected in pairs if (actual := phonemize(text)) != expected]


@pytest.mark.parametrize(("text", "expected"), read_cases())
def test_case(text, expected):
    assert phonemize(text) == expected


def test_every_spellchecker_word_matches_the_snapshot():
    with open(TESTS / "snapshot.dic", encoding="utf-8") as f:
        pairs = [line.rstrip("\n").split("\t") for line in f]
    assert mismatches(pairs)[:20] == []


def test_every_phrase_matches_the_snapshot():
    with open(TESTS / "phrases.dic", encoding="utf-8") as f:
        pairs = [line.rstrip("\n").split(" -> ") for line in f]
    assert mismatches(pairs)[:20] == []


def test_separator_goes_between_phones_but_not_inside_long_or_nasal_vowels():
    # Nasal vowels are a letter plus U+0303 (combining tilde), never a precomposed õ.
    assert phonemize("bouônjour, bouonne gens.", "|") == "b|w|o\u0303ː|ʒ|u|r b|w|ɔ|n ʒ|ɑ\u0303"


def test_separator_does_not_carry_over_to_the_next_call():
    phonemize("bouônjour", "|")
    assert phonemize("bouônjour") == "bwo\u0303ːʒur"
