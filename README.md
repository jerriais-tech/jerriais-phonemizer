# Jèrriais phonemiser

Turns Jèrriais (Jersey Norman French) text into IPA. The rules are written in
[Snowball](https://snowballstem.org/) (`src/*.sbl`) and compiled to Python, JavaScript and C.
The output suits TTS and alignment: affricates are single symbols (ʧ, ʤ), and long vowels and
diphthongs are marked with ː (eːi, oːu).

## Python

```sh
pip install "jerriais-phonemizer @ git+https://github.com/jerriais-tech/jerriais-phonemizer@v1.0.0"
```

```python
from jerriais_phonemizer import phonemize

phonemize("bouônjour, bouonne gens.")       # 'bwõːʒur bwɔn ʒɑ̃'
phonemize("bouônjour, bouonne gens.", "|")  # 'b|w|õː|ʒ|u|r b|w|ɔ|n ʒ|ɑ̃'
```

Input should be lowercase: uppercase letters are dropped, like punctuation.

## Building

`make` fetches and builds Snowball at the release pinned in the `Makefile` (`SNOWBALL_VERSION`),
then compiles the rules for every language. The Python package's generated files
(`python/jerriais_phonemizer/_snowball/`) are committed, so after changing a `.sbl` file run
`make python` and commit the result.

- `make test`: the Python tests (`tests/test_cases.csv`, plus the two snapshots).
- `make snapshot`: regenerate `tests/snapshot.dic` (the spellchecker's word list) and
  `tests/phrases.dic` from the C build. Do this only to accept a rule change, and read the diff.
- `make docs`: copy the JavaScript build into `docs/js/` for the demo page.

## Licence

AGPL-3.0 (`LICENSE`). The Snowball runtime files in `python/jerriais_phonemizer/_snowball/` are
under Snowball's BSD licence (`COPYING` there).
