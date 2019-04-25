# coding: utf-8
# Wikipedia記事のJSONファイルを読み込み，
#「イギリス」に関する記事本文を表示せよ．

import gzip, json

file_name = 'jawiki-country.json.gz'

with gzip.open(file_name, mode='rt') as data:
	for line in data:
		l = json.loads(line)
		if l['title'] == 'イギリス':
			print(l['text'])