#与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

def bi_gram(target, n):
	result = []
	for i in range(0, len(target)-n+1):
		result.append(target[i:i+n])
	return result

# 単語bi-gram
sentence = "I am an NLPer"
target = sentence.split(' ')
result = bi_gram(target, 2)
print(result)

# 文字bi-gram
target = sentence.replace(' ', '')
result = bi_gram(target, 2)
print(result)
