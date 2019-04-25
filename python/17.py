# 1列目の文字列の種類（異なる文字列の集合）を求めよ．
# 確認にはsort, uniqコマンドを用いよ．

result = []

with open('hightemp.txt') as txt_data:
	for line in txt_data:
		word = line.split('\t')[0]
		if word not in result:
			result.append(word)
	print(result)