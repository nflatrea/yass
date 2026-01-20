APP := yass.py

all: build

clean:
	rm -rf public
	
build:
	mkdir -p public
	python yass.py
	cp -rf static public/static/

run: build
	python -m http.server -d public

.PHONY: clean
