# 正規表現(regular expression)
# 文字列をパターンにて表現するもの
# そのパターンにマッチしているか、
# 否かの判定を行える
import re

# パターンの記述には raw stringが推奨
# 正規表現にて[\]が特殊文字のため、
# pyhtonと喧嘩しないように
pattern = r'これは\nraw string'
print(pattern)

pattern = r'a'
str = 'a'

# パターンマッチングの検証は
# re.matchを用いる
# 戻り値は、マッチ時に「マッチオブジェクト」
# ミスマッチ時は「Noneオブジェクト」
# になる
# ※オブジェクト...物
print(re.match(pattern, str))

str = 'b'
print(re.match(pattern, str))

# if でこれ判定する
# matchオブジェクト → True
# Noneオブジェクト → False
if re.match(r'a', 'a'):
  print('match')

else:
  print('miss match')

if re.match(r'a', 'b'):
  print('match')

else:
  print('miss match')

# match は先頭がマッチするかを判定する
print(re.match(r'a', 'abc'))
print(re.match(r'b', 'abc'))
print(re.match(r'c', 'abc'))

# search は先頭縛り無し。※こっちが一般的
print(re.search(r'a', 'abc'))
print(re.search(r'b', 'abc'))
print(re.search(r'c', 'abc'))

# 大文字/小文字は既定では区割される
print(re.search(r'ABC', 'abc'))
print(re.search(r'ABC', 'AbC', re.IGNORECASE)) # これで大文字、小文字が区別されなくなる

# メタ文字
# 正規表現で特殊な意味を持つ文字
# ^ …先頭
# $ …末尾
# . …任意の1文字
print('^$.')
print(re.search(r'^abc', 'abc'))
print(re.search(r'^abc', 'aabc')) # 先頭にabcがある
print(re.search(r'^.abc', 'aabc'))
print(re.search(r'^.abc', 'babc')) # miss
print(re.search(r'abc$', 'babc'))
print(re.search(r'abc$', 'xxxabcx')) # miss
print(re.search(r'...abc$', 'xxxabc'))
print(re.search(r'..abc$', 'xxxabc'))
print(re.search(r'....abc$', 'xxxabc'))
print(re.search(r'^..abc$', 'xxxabc'))

# 繰り返し指定のメタ文字
# 「直前の文字が」何回繰り返すかを
# 指定することができる
# + ... 1回以上
# * ... 0回以上
# ? ... 0回か、1回
# {m} ... m回
# {m,n} ... m回以上、n回以下
# {m,} ... m回以上
# {,n} ... n回以下
print('+*?{m}')
print(re.search(r'a+bc', 'abc'))
print(re.search(r'a+bc', 'aaabc'))
print(re.search(r'a+bc', 'bc')) # miss

print(re.search(r'a*bc', 'abc'))
print(re.search(r'a*bc', 'aaabc'))
print(re.search(r'a*bc', 'bc'))

print(re.search(r'a?bc', 'bc'))
print(re.search(r'a?bc', 'abc'))
print(re.search(r'a?bc', 'aabc'))
print(re.search(r'^a?bc', 'aabc')) # miss

print(re.search(r'a{3}bc', 'aaabc'))
print(re.search(r'a{3}bc', 'aabc')) # miss
print(re.search(r'a{3}bc', 'aaaabc'))
print(re.search(r'^a{3}bc', 'aaaabc')) # miss

print(re.search(r'.{3}bc', 'aaabc'))
print(re.search(r'.{3}bc', 'abcbc'))
print(re.search(r'.{3}bc', 'bcbc')) # miss

print(re.search(r'a{2,4}bc', 'abc')) # miss
print(re.search(r'a{2,4}bc', 'aabc'))
print(re.search(r'a{2,4}bc', 'aaabc'))
print(re.search(r'a{2,4}bc', 'aaaabc'))
print(re.search(r'a{2,4}bc', 'aaaaaaaabc'))
print(re.search(r'^a{2,4}bc', 'aaaaaaaabc'))

print(re.search(r'a{2,}bc', 'abc')) # miss
print(re.search(r'a{2,}bc', 'aabc'))
print(re.search(r'a{2,}bc', 'aaabc'))
print(re.search(r'^a{2,}bc', 'aaaaaaabc'))

print(re.search(r'a{,2}bc', 'bc'))
print(re.search(r'a{,2}bc', 'abc'))
print(re.search(r'a{,2}bc', 'aaaaabc'))

# 文字集合
# [] … 何これ
print('[]')
print(re.search(r'[abc]bc', 'abc'))
print(re.search(r'[abc]bc', 'bbc'))
print(re.search(r'[abc]bc', 'cbc'))
print(re.search(r'[abc]bc', 'dbc')) # miss
print(re.search(r'[abc]bc', 'bc')) # miss

print(re.search(r'b-c', 'b-c'))
print(re.search(r'b-c', 'bc')) # miss

print(re.search(r'[a-c]bc', 'abc')) # []内の-は、範囲指定になるので注意
print(re.search(r'[a-c]bc', 'bbc'))
print(re.search(r'[a-c]bc', 'cbc'))
print(re.search(r'[a-c]bc', 'dbc')) # miss

print(re.search(r'[0123456789]', '5'))
print(re.search(r'[0-9]', '5'))
print(re.search(r'[a-z]', 'x'))
print(re.search(r'[A-Z]', 'X'))
print(re.search(r'[a-zA-Z]', 'X'))
print(re.search(r'[0-9a-zA-Z]', 'X'))

print(re.search(r'\d', '5')) # 数値※[0-9０-９]と同じ
print(re.search(r'\d', '５'))
print(re.search(r'\d', 'a')) # miss
print(re.search(r'\D', 'a')) # 数値以外
print(re.search(r'\D', 'あ'))
print(re.search(r'\D', '2')) # miss
print(re.search(r'\s', ' ')) # 空白文字
print(re.search(r'\s', '\n'))
print(re.search(r'\s', '\t'))
print(re.search(r'\S', 'あ')) # 空白文字以外
print(re.search(r'\bis\b', 'this is')) # \b で単語の区切り
print(re.search(r'\bis\b', 'this')) # miss

# 単語選択
# (abc | def)
print('(abc|def)')
print(re.search(r'color | colour', 'color'))
print(re.search(r'color | colour', 'colour'))
print(re.search(r'colou?r', 'color'))

# グループ
# () …グループ化することにより
# .groupや .groupsで取得可能
match = re.search(r'(\d{4})/(\d{1,2})/(\d{1,2})','2025/4/28')
if match:
  print(match.group(0)) # 全体
  print(match.group(1)) # 年
  print(match.group(2)) # 月
  print(match.group(3)) # 日
  print(match.groups()) # 全てのグループを取得

# 打消しは「\」
print('打消し')
print(re.search(r'\^', '^'))
print(re.search(r'\$', '$'))
print(re.search(r'\+', '+'))
print(re.search(r'\*', '*'))

print(re.search(r'\?', '?'))
print(re.search(r'\{', '{'))
print(re.search(r'\(', '('))
print(re.search(r'\|', '|'))

print(re.search(r'[0\-9]', '-'))
print(re.search(r'[0\-9]', '5')) # miss
print(re.search(r'\\', '\\'))

# 最短一致
# +? …手前の文字が1回以上(最短)
# *? …手前の文字が0回以上(最短)
print('+?*?')
print(re.search(r'.+', 'abc'))
print(re.search(r'.+?', 'abc')) # 最短
print(re.search(r'.*', 'abc'))
print(re.search(r'.*?', 'abc')) # 最短

print(re.search(r'aaa.*?aaa', 'aaabbbaaacccaaa')) # 最短
print(re.search(r'aaa.*?aaa', 'aaaaaacccaaa')) # 最短
print(111111111111111111111111111111)

# Matchオブジェクト
print('Match object')
match = re.search(r'ccc', 'abccc')
print(match.start())
print(match.end())
print(match.span())

match = re.search(r'ccc', 'abcccdccc')
print(match.span())

# → 最初に見つかった場合場所のみ

# 複数マッチ(文字列リスト取得)はfindall
print('findall')
print(re.findall(r'ccc', 'abcccdccc'))

# 複数マッチ(Matchオブジェクトイテレータ取得)はfinditer
# ※イテレーター…forでぶん回せる
print('finditer')
for match in re.finditer(r'ccc', 'abcccdccc'):
  print(match.span())

# かぶりは
for match in re.finditer(r'ccc', 'abccccc'):
  print(match.span())

for match in re.finditer(r'ccc', 'abcccccc'):
  print(match.span())

# →かぶりはは無し

# マッチした箇所で区切ってリスト化
print('list化')
print(re.split(r',', 'aaa,bbb,ccc'))

# マッチした箇所を置換
print('replace')
print(re.sub(r',', ':', 'aaa,bbb,ccc'))

# 先読み / 後読み
# (?=) …先読み
# (?!) …否定先読み
# (?<=) …後読み
# (?<!) …否定後読み
# 先頭を表す^や、末尾の$と同じ扱い
# パターンマッチングはするが、
# 結果のマッチオブジェクトには含まれない

# 先読み(右側をチェック)
print(re.search(r'python(?=flask)', 'pythonflask'))
print(re.search(r'python(?=flask)', 'python')) # miss

# →右側にflaskがあるものだけマッチ
print(re.search(r'python(?=flask)', 'pythonflask'))
print(re.search(r'python(?=flask)', 'python')) # miss


# 否定先読み
print(re.search(r'python(?!flask)', 'pythonflask')) # miss
print(re.search(r'python(?!flask)', 'python'))

# →右側にflaskがないものだけマッチ
print(re.search(r'python(?!flask)', 'python'))

# 後読み(左側をチェック)
print(re.search(r'(?<=python)flask', 'pythonflask'))
print(re.search(r'(?<=python)flask', 'python')) # miss
# →側にflaskがないものだけマッチ

# →左側にpythonがあるものだけマッチ
print(re.search(r'(?<=python)flask', 'pythonflask'))
print(re.search(r'(?<=python)flask', 'python')) # miss
# →左側にflaskがないものだけマッチ

# 否定後読み (左側をチェック)
print(re.search(r'(?<!python)flask', 'pythonflask')) # miss
print(re.search(r'(?<!python)flask', 'flask'))
# →左側にpythonがないものだけマッチ

# 先読み/後読み + グループ
print(re.search(r'新宿(?=(駅|区))', '新宿駅'))
print(re.search(r'新宿(?=(駅|区))', '新宿区'))
print(re.search(r'新宿(?=(駅|区))', '新宿')) # miss

print(re.search(r'新宿(?=(駅|御苑))', '新宿駅')) # 先読みの可変長はOK
print(re.search(r'新宿(?=(駅|御苑))', '新宿御苑'))

print(re.search(r'(?<=)(西|東)', '西新宿'))
# print(re.search(r'(?<=)(西|北東)', '西新宿')) # 後読みの可変長はNG

# 先読み(後読み)の活用事例その１
print(re.sub(r'日本(?=語)', '国', '日本では日本語と英語を勉強する。'))

# 先読み(後読み)の活用事例その2(タブ取得)
print(re.findall(r'(?<=#)\S', '#aaa #bbb #ccc'))

# 後読み(左側)記載
print(re.search(r'(?=pythonflask)python', 'pythonflask'))
print(re.search(r'(?=pythonflask)a', 'pythonflaska')) # miss

# →あらかじめ、先読み指定パターンが存在することをチェックし、
# 存在した場合、右側のパターンを、存在した場所の先頭からチェックする
# 後読みの場合、存在した場所の"先頭から"、にならない
# #存在した場所より"右側から"、となる
print(re.search(r'(?<=pythonflask)a', 'pythonflaska'))

# 先読み(後読み)の活用事例その3
# 任意条件(今回は３文字)に加え
# 英字大文字が含まれている?
pattern = r'(?=.*?[A-Z]).{3}'
print(re.search(pattern, 'Abc'))
print(re.search(pattern, 'aBc'))
print(re.search(pattern, 'abC'))
print(re.search(pattern, 'ABC'))
print(re.search(pattern, 'abc')) # miss

# 先読み(後読み)の活用事例その4
# 任意条件(今回は３文字)に加え
# 英字大文字及び、小文字が含まれている?
pattern = r'(?=.*?[a-z])(?=.*?[A-Z]).{3}'
print(re.search(pattern, 'Abc'))
print(re.search(pattern, 'AAA')) # miss
print(re.search(pattern, 'aaa')) # miss
print(re.search(pattern, '123')) # miss
# (?=)(?=)の様に、先読みが連続した場合、
# AND条件となり、全てを満たす必要がある

# 先読み(後読み)の活用事例その5
# パスワードは半角英字及び記号(.または_)にて
# 構成され、少なくとも５桁必要
# また、英文字、小文字、数値、記号(._)の
# 全てを含むこと
pattern = r'^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[_.])[0-9a-zA-Z_.]{5,}$'
print(re.search(pattern, 'aA0_a'))
print(re.search(pattern, 'aA0.a'))
print(re.search(pattern, 'aA0.aa'))

print(re.search(pattern, 'aA0.')) # miss
print(re.search(pattern, 'AA0.0')) # miss
print(re.search(pattern, 'aa0.0')) # miss

print(re.search(pattern, 'aaA.A')) # miss
print(re.search(pattern, 'aaA0A')) # miss
print(re.search(pattern, 'aA0_a@')) # miss 必須文字の制約は通るが、利用可能文字の「[0-9a-zA-Z_.]{5,}」でOUT。

# ～おまけ～
# []内でエスケープが必要なのは以下。
# \ -> \\
# ] -> \]
# - -> \-
# ^ -> \^ ※[]内の先頭の^は、否定。[^abc]で、abc以外。
# その他、.*+?{}()|はエスケープせずに使える。