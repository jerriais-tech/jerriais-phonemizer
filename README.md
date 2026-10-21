# Jèrriais phonemiser

A phonemiser for Jèrriais (Jersey Norman French), written in [Snowball](https://snowballstem.org/).
The rules in `src/*.sbl` are the source; Snowball compiles them to Python, JavaScript and C.
The output suits TTS and alignment: affricates are single symbols (ʧ, ʤ), and long vowels and
diphthongs are marked with ː (eːi, oːu).

## Python

```sh
pip install jerriais-phonemizer
```

```python
from jerriais_phonemizer import phonemize

phonemize("bouônjour, bouonne gens.")       # 'bwõːʒur bwɔn ʒɑ̃'
phonemize("bouônjour, bouonne gens.", "|")  # 'b|w|õː|ʒ|u|r b|w|ɔ|n ʒ|ɑ̃'
```

Input should be lowercase: uppercase letters are dropped, like punctuation. Nasal vowels come out
as a letter plus U+0303 (combining tilde), never precomposed (õ).

## JavaScript and C

`make javascript` writes `dist/javascript/phonemizer.js` (the class is the default export; call
`new Phonemizer().phonemize(text)`), and `make c_example` builds a command-line tool,
`dist/c/phonemizewords`, that phonemises a file of words or phrases one per line. These aren't
published as packages.

## Building

`make` fetches and builds Snowball at the release pinned in the `Makefile` (`SNOWBALL_VERSION`),
then compiles the rules for every language. The Python package's generated files
(`python/jerriais_phonemizer/_snowball/`) are committed, so after changing a `.sbl` file run
`make python` and commit the result.

- `make test`: the Python tests (`tests/test_cases.csv`, plus the two snapshots).
- `make snapshot`: regenerate `tests/snapshot.dic` (the spellchecker's word list) and
  `tests/phrases.dic` from the C build. Do this only to accept a rule change, and read the diff.

## Releasing

Bump `version` in `pyproject.toml`, commit, tag (`vX.Y.Z`) and push the tag. Then run the
"Publish to PyPI" workflow (Actions tab) with that tag: it builds the wheel and sdist from the tag
and uploads them to PyPI by trusted publishing.

## Test data

- `tests/jerriais.dic`: the Jèrriais spellchecker word list from the Société Jersiaise's
  [spellchecker page](https://members.societe-jersiaise.org/sdllj/spellchecker.html), one word per line.
  `tests/snapshot.dic` is its phonemisation.
- `tests/phrases.txt`: example phrases, some of them transcripts of Geraint Jennings's recordings.
  `tests/phrases.dic` is their phonemisation.

The sdist leaves out the word list and its snapshot (3.6 MB); the test that uses them skips without them.

## Licence

GNU Affero General Public License, version 3 or (at your option) any later version
(`AGPL-3.0-or-later`, `LICENSE`). If you run a modified version as a network service, the AGPL asks
you to offer its source to the service's users. The Snowball runtime files in
`python/jerriais_phonemizer/_snowball/` are under Snowball's BSD licence (`COPYING` there).
