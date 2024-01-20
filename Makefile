.PHONY: all
all: clean schema install dict convert2fly

clean:
	rm -f build/*

schema:
	mkdir -p build && cp -f src/radical_pinyin.schema.yaml build/radical_pinyin.schema.yaml

install:
	pip install -r requirements.txt

dict: install
	python build.py

convert2fly: dict
	python convert_dict.py build/dict.yaml build/radical_pinyin_flypy.dict.yaml tofly "'"
