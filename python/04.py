# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
one_word_filter = [1, 5, 6, 7, 8, 9, 15, 16, 19]
words = sentence.split(' ')
ans = {}
for (num, word) in enumerate(words, 1):
	if num in one_word_filter:
		ans[word[0:1]] = num
	else:
		ans[word[0:2]] = num
	pass

print(ans)