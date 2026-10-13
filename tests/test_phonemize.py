import csv
from pathlib import Path

import pytest

from jerriais_phonemizer import phonemize

TESTS = Path(__file__).parent


def read_cases():
    with open(TESTS / "test_cases.csv", newline="", encoding="utf-8") as f:
        return [(row["input"], row["expected_output"]) for row in csv.DictReader(f)]


def read_pairs(name, separator):
    with open(TESTS / name, encoding="utf-8") as f:
        return [line.rstrip("\n").split(separator) for line in f]


def first_mismatches(pairs, n=20):
    out = [(text, expected, actual) for text, expected in pairs if (actual := phonemize(text)) != expected]
    return out[:n]


@pytest.mark.parametrize(("text", "expected"), read_cases())
def test_word_gives_the_ipa_vits_was_trained_on(text, expected):
    assert phonemize(text) == expected


def test_every_spellchecker_word_matches_the_snapshot():
    assert first_mismatches(read_pairs("snapshot.dic", "\t")) == []


def test_every_phrase_matches_the_snapshot():
    assert first_mismatches(read_pairs("phrases.dic", " -> ")) == []


def test_separator_goes_between_phones_and_length_and_nasal_marks_stay_on_their_vowel():
    # Nasal vowels are a letter plus U+0303 (combining tilde), never a precomposed õ.
    assert phonemize("bouônjour, bouonne gens.", "|") == "b|w|o\u0303ː|ʒ|u|r b|w|ɔ|n ʒ|ɑ\u0303"


def test_separator_does_not_carry_over_to_the_next_call():
    phonemize("bouônjour", "|")
    assert phonemize("bouônjour") == "bwo\u0303ːʒur"
