#スペースで区切られた単語列に対して，
#各単語の先頭と末尾の文字は残し，
#それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
#ただし，長さが４以下の単語は並び替えないこととする．
#適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，
#その実行結果を確認せよ．

# coding: utf-8
import random

def Typoglycemia(target):
	'''タイポグリセミア
	スペースで区切られた単語列に対して、各単語の先頭と末尾の文字は残し、
	それ以外の文字の順序をランダムに並び替える。
	ただし、長さが４以下の単語は並び替えない。

	引数:
	target -- 対象の文字列
	戻り値:
	変換した文字列
	'''
	result = []
	for word in target.split(' '):
		if len(word) <= 4:
			result.append(word)
		else:
			chr_list = list(word[1:-1])
			random.shuffle(chr_list)
			result.append(word[0] + ''.join(chr_list) + word[-1])

	return ' '.join(result)

def Typoglycemia2(target):
	'''ジェネレータを使ったもの
	上記だとリストを作ってしまっているがこっちは作らずに済む
	'''
	def words():
		for word in target.split():
			if len(word) <= 4:
				yield word
			else:
				middle = list(word[1:-1])
				random.shuffle(middle)
				yield word[0] + ''.join(middle) + word[-1]
	return ' '.join(words())

# 対象文字列の入力
target = input('文字列を入力してください--> ')

# タイポグリセミア
result = Typoglycemia2(target)
print('変換結果:' + result)