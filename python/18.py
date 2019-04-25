# coding: utf-8

# 各行を3カラム目の数値の逆順で整列せよ
#（注意: 各行の内容は変更せずに並び替えよ）．
# 確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

lines = open('hightemp.txt').readlines()

lines.sort(key=lambda line: float(line.split('\t')[2]), reverse=True)

for line in lines:
	print(line, end='')