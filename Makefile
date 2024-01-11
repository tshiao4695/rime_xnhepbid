.PHONY: all
all: clean install dict

clean:
	rm -f build/*

install:
	pip install -r requirements.txt

dict:
	python build.py
