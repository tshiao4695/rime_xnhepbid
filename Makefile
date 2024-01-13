.PHONY: all
all: clean schema install dict

clean:
	rm -f build/*

schema:
	mkdir -p build && cp -f src/radical_pinyin.schema.yaml build/radical_pinyin.schema.yaml

install:
	pip install -r requirements.txt

dict:
	python build.py
