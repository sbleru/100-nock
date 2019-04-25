# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

with open('hightemp.txt') as data:
	for line in data:
		print(line.replace('\t', ' '), end='') #line自体に改行があるので改行しないようにする