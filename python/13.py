# 12で作ったcol1.txtとcol2.txtを結合し，
# 元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
# 確認にはpasteコマンドを用いよ．

with open('col1.txt') as col1_data, \
		open('col2.txt') as col2_data, \
		open('merge.txt', mode='w') as merge_txt:
	for c1, c2 in zip(col1_data, col2_data):
		merge_txt.write(c1.rstrip()+'\t'+c2.rstrip()+'\n');