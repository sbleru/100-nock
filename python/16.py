# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のファイルを行単位でN分割せよ．
# 同様の処理をsplitコマンドで実現せよ．

n = int(input('N-->'))

with open('hightemp.txt') as txt_data:
	lines = txt_data.readlines()

count = len(lines)
unit = count//n

for i, offset in enumerate(range(0, count, unit), 1):
	with open('split_{:02d}.txt'.format(i), mode='w') as out_file:
		for line in lines[offset:offset+unit]:
			out_file.write(line)
			pass