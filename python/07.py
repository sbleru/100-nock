# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ

from string import Template

def format_string(x,y,z):
	s = Template('$hour時の$targetは$value')
	return s.substitute(hour=x, target=y, value=z)
	pass

x = 12
y = '気温'
z = 22.4
print(format_string(x, y, z))