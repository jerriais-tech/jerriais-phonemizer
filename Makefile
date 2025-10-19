all: javascript python docs c c_example

srcs = dist/c/phonemizer.c dist/c/examples/api.c dist/c/examples/phonemizewords.c dist/c/examples/utilities.c
headers = dist/c/phonemizer.h dist/c/examples/api.h dist/c/examples/header.h
sbl_src = src/jerriais-phonemizer.sbl src/ent-words.sbl

c_example: dist/c/phonemizewords

dist/c/phonemizewords: $(srcs) $(headers)
	gcc dist/c/phonemizer.c dist/c/examples/*.c -I./dist/c -I./dist/c/examples -o dist/c/phonemizewords

c: dist/c/phonemizer.c dist/c/phonemizer.h

javascript: dist/javascript/phonemizer.js

python: dist/python/phonemizer.py

docs: docs/js/base-stemmer.js docs/js/phonemizer.js docs/index.html

test: python tests/test_cases.csv snapshot
	python tests/test.py

snapshot: tests/snapshot.dic

tests/snapshot.dic: dist/c/phonemizewords tests/jerriais.dic
	./dist/c/phonemizewords -i tests/jerriais.dic -o tests/snapshot.dic -p

docs/js/base-stemmer.js docs/js/phonemizer.js: javascript
	cp dist/javascript/base-stemmer.js dist/javascript/phonemizer.js docs/js

dist/c/phonemizer.c dist/c/phonemizer.h: $(sbl_src)
	snowball src/jerriais-phonemizer.sbl -o dist/c/phonemizer -utf8

dist/javascript/phonemizer.js: $(sbl_src)
	snowball src/jerriais-phonemizer.sbl -js -o dist/javascript/phonemizer

dist/python/phonemizer.py: $(sbl_src)
	snowball src/jerriais-phonemizer.sbl -py -o dist/python/phonemizer
