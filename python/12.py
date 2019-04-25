# 各行の1列目だけを抜き出したものをcol1.txtに，
# 2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
# 確認にはcutコマンドを用いよ．

with open('hightemp.txt') as data, \
		open('col1.txt', mode='w') as col1_file, \
		open('col2.txt', mode='w') as col2_file:
	for line in data:
		col = line.split('\t');
		col1_file.write(col[0] + '\n')
		col2_file.write(col[1] + '\n')
		pass