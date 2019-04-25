# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

import gzip, json, re

def extract_England():

	file_name = 'jawiki-country.json.gz'

	with gzip.open(file_name, mode='rt') as countries_data:
		for line in countries_data:
			country_data = json.loads(line)
			if country_data['title'] == 'イギリス':
				return country_data['text']

	raise ValueError('見つかりませんでした')

pattern = re.compile('^\[\[.*Category:(.*?)(?:\|.*)?\]\].*$', re.MULTILINE)

en_data = extract_England()

category = pattern.findall(en_data)

for line in category:
	print(line)