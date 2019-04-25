# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ
# coding: utf-8
import gzip, json, re

fname = 'jawiki-country.json.gz'

def extract_UK():
	'''イギリスに関する記事本文を取得

	戻り値：
	イギリスの記事本文
	'''

	with gzip.open(fname, 'rt') as data_file:
		for line in data_file:
			data_json = json.loads(line)
			if data_json['title'] == 'イギリス':
				return data_json['text']

	raise ValueError('イギリスの記事が見つからない')


# 基礎情報テンプレートの抽出条件のコンパイル
pattern = re.compile(r'''
	^\{\{基礎情報(.*?)\}\}$
	''', re.MULTILINE + re.VERBOSE + re.DOTALL)

# 基礎情報テンプレートの抽出
contents = pattern.findall(extract_UK())

pattern = re.compile(r'''
	^\|(.+?)\s\=\s(.+?)(?:(?=\n\|)|(?=\n$))
	''', re.MULTILINE + re.VERBOSE + re.DOTALL)

contents_dict = pattern.findall(contents[0])

for line in contents_dict:
	print(line)