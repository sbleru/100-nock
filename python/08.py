# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

# ジェネレータ内包表記
def cipher2(target):
	#joinは文字列連結 joinを使うのはprintを使うため?
	result = ''.join((chr(219 - ord(c)) if c.islower() else c for c in target))
	return result

def cipher3(target):
	result = ''
	for c in target:
		result += chr(219 - ord(c)) if c.islower() else c
	return result

def cipher(target):
	result=''
	for chara in target:
		if chara.islower():
			result += chr(219-ord(chara))
		else:
			result += chara
	return result
	pass

target = input('文字列入力してください\n>>> ')
#暗号化
crypted_text = cipher(target)
print(crypted_text)
#復号化
decrypted_text = cipher(crypted_text)
print(decrypted_text)

#暗号化
crypted_text = cipher2(target)
print(crypted_text)
#復号化
decrypted_text = cipher2(crypted_text)
print(decrypted_text)