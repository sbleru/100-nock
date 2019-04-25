# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ

def bi_gram(target, n):
	result = []
	for i in range(0, len(target)-n+1):
		result.append(target[i:i+n])
	return result

word1 = "paraparaparadise"
word2 = "paragraph"
X = set(bi_gram(word1, 2))
Y = set(bi_gram(word2, 2))

print('X:' + str(X))
print('Y:' + str(Y))

print('union:' + str(X|Y))
print('intersection:' + str(X&Y))
print('difference:' + str(X-Y))

print('se in X? ' + str('se' in X))
print('se in Y? ' + str('se' in Y))