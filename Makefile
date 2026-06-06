all: javascript python docs c c_example

srcs = dist/c/phonemizer.c dist/c/examples/api.c dist/c/examples/phonemizewords.c dist/c/examples/utilities.c
headers = dist/c/phonemizer.h dist/c/examples/api.h dist/c/examples/header.h
sbl_src = src/jerriais-phonemizer.sbl src/stringdefs.sbl src/silent_nt.sbl src/silent_h.sbl src/liaison.sbl src/special-case.sbl src/phonemes.sbl

c_example: dist/c/phonemizewords

dist/c/phonemizewords: $(srcs) $(headers)
	gcc dist/c/phonemizer.c dist/c/examples/*.c -I./dist/c -I./dist/c/examples -o dist/c/phonemizewords

c: dist/c/phonemizer.c dist/c/phonemizer.h

javascript: dist/javascript/phonemizer.js

python: dist/python/phonemizer.py

docs: javascript

test: python tests/test_cases.csv snapshot
	python tests/test.py

snapshot: tests/snapshot.dic tests/phrases.dic

tests/snapshot.dic tests/phrases.dic: dist/c/phonemizewords tests/jerriais.dic tests/phrases.txt
	./dist/c/phonemizewords -i tests/jerriais.dic -o tests/snapshot.dic -p2
	./dist/c/phonemizewords -i tests/phrases.txt -o tests/phrases.dic -p

docs/js/phonemizer.js: javascript

dist/c/phonemizer.c dist/c/phonemizer.h: $(sbl_src)
	snowball src/jerriais-phonemizer.sbl -o dist/c/phonemizer -utf8

dist/javascript/phonemizer.js: $(sbl_src)
	snowball src/jerriais-phonemizer.sbl -js -o dist/javascript/phonemizer

dist/python/phonemizer.py: $(sbl_src)
	snowball src/jerriais-phonemizer.sbl -py -o dist/python/phonemizer
