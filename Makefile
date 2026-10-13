all: javascript python c c_example

# Snowball is fetched and built at this upstream release; nothing uses a snowball on the PATH.
SNOWBALL_VERSION = v3.1.1
snowball_dir = build/snowball-$(SNOWBALL_VERSION)
snowball = $(snowball_dir)/snowball

sbl_src = src/jerriais-phonemizer.sbl src/stringdefs.sbl src/silent_nt.sbl src/silent_h.sbl src/liaison.sbl src/special-case.sbl src/phonemes.sbl
py_pkg = python/jerriais_phonemizer/_snowball

$(snowball):
	rm -rf $(snowball_dir)
	git clone --quiet --depth 1 --branch $(SNOWBALL_VERSION) https://github.com/snowballstem/snowball $(snowball_dir)
	$(MAKE) -C $(snowball_dir) snowball

c_example: dist/c/phonemizewords

# api.h and the runtime come from the Snowball checkout.
dist/c/phonemizewords: dist/c/phonemizer.c dist/c/phonemizer.h dist/c/examples/phonemizewords.c
	gcc dist/c/phonemizer.c dist/c/examples/phonemizewords.c $(snowball_dir)/runtime/*.c -I./dist/c -I$(snowball_dir)/runtime -o dist/c/phonemizewords

c: dist/c/phonemizer.c dist/c/phonemizer.h

javascript: dist/javascript/phonemizer.js dist/javascript/base-stemmer.js

# The Python package commits its generated files, so it installs from git without Snowball.
python: $(py_pkg)/phonemizer.py $(py_pkg)/basestemmer.py $(py_pkg)/among.py $(py_pkg)/COPYING

test: python
	uv run pytest

# The snapshots are expected outputs: regenerate them only to accept a rule change.
snapshot: tests/snapshot.dic tests/phrases.dic

tests/snapshot.dic tests/phrases.dic: dist/c/phonemizewords tests/jerriais.dic tests/phrases.txt
	./dist/c/phonemizewords -i tests/jerriais.dic -o tests/snapshot.dic -p2
	./dist/c/phonemizewords -i tests/phrases.txt -o tests/phrases.dic -p

dist/c/phonemizer.c dist/c/phonemizer.h: $(sbl_src) $(snowball)
	$(snowball) src/jerriais-phonemizer.sbl -o dist/c/phonemizer -utf8

dist/javascript/phonemizer.js: $(sbl_src) $(snowball)
	$(snowball) src/jerriais-phonemizer.sbl -js -o dist/javascript/phonemizer

dist/javascript/base-stemmer.js: $(snowball)
	cp $(snowball_dir)/javascript/base-stemmer.js $@

$(py_pkg)/phonemizer.py: $(sbl_src) $(snowball)
	$(snowball) src/jerriais-phonemizer.sbl -py -o $(py_pkg)/phonemizer

$(py_pkg)/basestemmer.py $(py_pkg)/among.py: $(snowball)
	cp $(snowball_dir)/python/snowballstemmer/$(notdir $@) $@

$(py_pkg)/COPYING: $(snowball)
	cp $(snowball_dir)/COPYING $@

.PHONY: all c c_example javascript python test snapshot
