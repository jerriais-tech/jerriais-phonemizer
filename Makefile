all: javascript python

javascript: dist/javascript/phonemizer.js

python: dist/python/phonemizer.py

test: python tests/test_cases.csv
	python tests/test.py

dist/javascript/phonemizer.js: src/jerriais-phonemizer.sbl
	snowball src/jerriais-phonemizer.sbl -js -o dist/javascript/phonemizer

dist/python/phonemizer.py: src/jerriais-phonemizer.sbl
	snowball src/jerriais-phonemizer.sbl -py -o dist/python/phonemizer
