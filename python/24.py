# 記事から参照されているメディアファイルをすべて抜き出せ．
# [[ファイル:Wiki.png|thumb|説明文]]

import gzip, json, re

def extract_England():

	file_name = 'jawiki-country.json.gz'

	with gzip.open(file_name, mode='rt') as countries_data:
		for line in countries_data:
			country_data = json.loads(line)
			if country_data['title'] == 'イギリス':
				return country_data['text']

	raise ValueError('見つかりませんでした')

pattern = re.compile(r'''
	.*(?:File|ファイル):(.+?)\|.*
	''', re.MULTILINE + re.VERBOSE)

en_data = extract_England()

img_files = pattern.findall(en_data)

for line in img_files:
	print(line)