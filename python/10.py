# 行数をカウントせよ．確認にはwcコマンドを用いよ．

count = 0
with open('hightemp.txt') as data:
	for line in data:
		count += 1
		pass

print(count)