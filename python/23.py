# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．

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
	^
	(={2,})
	\s*
	(.+?)
	\s*
	\1
	.*
	$
	''', re.MULTILINE + re.VERBOSE)

en_data = extract_England()

category = pattern.findall(en_data)

for line in category:
	length = len(line[0]) - 1
	print('{indent}{sect}({level})'.format(
		indent='\t' * (length-1), 
		sect=line[1], 
		level=length))