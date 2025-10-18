all: javascript python docs

snapshot: tests/snapshot.dic

tests/snapshot.dic: dist/c/phonemizewords tests/jerriais.dic
	./dist/c/phonemizewords -i tests/jerriais.dic -o tests/snapshot.dic -p

c_example: dist/c/phonemizewords

srcs = dist/c/phonemizer.c dist/c/examples/api.c dist/c/examples/phonemizewords.c dist/c/examples/utilities.c
headers = dist/c/phonemizer.h dist/c/examples/api.h dist/c/examples/header.h

dist/c/phonemizewords: $(srcs) $(headers)
	gcc dist/c/phonemizer.c dist/c/examples/*.c -I./dist/c -I./dist/c/examples -o dist/c/phonemizewords

c: dist/c/phonemizer.c dist/c/phonemizer.h

javascript: dist/javascript/phonemizer.js

python: dist/python/phonemizer.py

docs: javascript
	cp dist/javascript/base-stemmer.js dist/javascript/phonemizer.js docs/js

test: python tests/test_cases.csv snapshot
	python tests/test.py

dist/c/phonemizer.c dist/c/phonemizer.h: src/jerriais-phonemizer.sbl
	snowball src/jerriais-phonemizer.sbl -o dist/c/phonemizer -utf8

dist/javascript/phonemizer.js: src/jerriais-phonemizer.sbl
	snowball src/jerriais-phonemizer.sbl -js -o dist/javascript/phonemizer

dist/python/phonemizer.py: src/jerriais-phonemizer.sbl
	snowball src/jerriais-phonemizer.sbl -py -o dist/python/phonemizer
