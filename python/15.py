# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のうち末尾のN行だけを表示せよ．
# 確認にはtailコマンドを用いよ．

file_name = 'hightemp.txt'
n = int(input('N-->'))

with open(file_name) as file_data:
	lines = file_data.readlines()
	for i in range(n, 0, -1):
		print(lines[-i].rstrip())