# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のうち先頭のN行だけを表示せよ．
# 確認にはheadコマンドを用いよ．

import sys

with open('hightemp.txt') as txt_data:
	for i, line in enumerate(txt_data):
		if i < int(sys.argv[1]):
			print(line, end='')
