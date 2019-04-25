# 各行の1列目の文字列の出現頻度を求め，
# その高い順に並べて表示せよ．
# 確認にはcut, uniq, sortコマンドを用いよ．

lines = open('hightemp.txt').readlines()

prefectures = {}
for line in lines:
	pref = line.split('\t')[0]
	if pref in prefectures:
		prefectures[pref] += 1
	else:
		prefectures[pref] = 1

pref_set = sorted(prefectures.items(), key=lambda x:x[1], reverse=True)

for pref in pref_set:
	print(pref)
