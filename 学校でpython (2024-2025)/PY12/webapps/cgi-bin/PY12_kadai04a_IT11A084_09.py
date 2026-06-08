############################################
#   Kadai04a-IT11A084-09 エリアッセンカスパ  #
############################################

# import the necessary tools
# 文字化け対策
import sys, io, cgi

# 出力のエンコーディングを設定
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='UTF-8')
print("Content-Type: text/html; charset=UTF-8")
print("")

# デバッグ用にエラーメッセージを表示
import cgitb
cgitb.enable()

# フォームから送られたデータを受け取る
rdata = cgi.FieldStorage()

# 正解の答え（フォームに隠し値として送られてくる）を取得
cvalue = rdata.getvalue("c", default="なし")

# カンマ区切りの正解の答えをリストに分割
answ = cvalue.split(',')

# 質問と選択肢のデータ（これは元の質問と選択肢が格納されている部分です）
Q = [
    {
        'question': '日本人の体温平均は36度ですが、グリーンランド人の体温平均は何度でしょうか?',
        'answers': [
            '35.7度',
            '36度',
            '36.3度',
            '37度'
        ],
        'correct': 3
    },{
        'question': 'グリーンランド人はいくつの言語勉強しますか?',
        'answers': [
            '1つ',
            '2つ',
            '3つ',
            '4つ'
        ],
        'correct': 2
    },{
        'question': 'グリーンランドは島ですか、それとも陸地ですか?',
        'answers': [
            '島',
            '陸地',
            '海',
            '氷山'
        ],
        'correct': 0
    },
    {
        'question': 'グリーンランドはどのくらいの大きさですか?',
        'answers': [
            '205.8万km²',
            '210.2万km²',
            '216.6万km²',
            '220万km²'
        ],
        'correct': 2
    },{
        'question': 'グリーンランドの人口は何人ですか?',
        'answers': [
            '約5万',
            '約8万',
            '約10万',
            '約15万'
        ],
        'correct': 0
    },{
        'question': 'グリーンランドから日本まで何キロ?',
        'answers': [
            '5千5百キロメートル',
            '7千3百キロメートル',
            '8千9キロメートル',
            '8千11キロメートル'
        ],
        'correct': 3
    }
]

# HTML出力
print(f'''
<html>
<head><title>課題4 フォムコントロール</title></head>
<body style="background-color: #ff99ff">
    <h3>回答画面 IT11A084 09 エリアッセン カスパ</h3>
''')

# 全ての質問についてユーザーの答えと正解を比較
for i in range(len(answ)):
    # ユーザーの答えを取得（文字列として取得されるので、整数に変換）
    user_answer = rdata.getvalue(f'q{i}', default=None)

    # ユーザーが答えを選ばなかった場合、Noneが返されるので、それに対処
    if user_answer is not None:
        user_answer = int(user_answer)

    # 正解の答えのインデックスを取得
    correct_answer_index = int(answ[i])
    
    # 正解の答えを文字列に変換（選択肢リストから取得）
    correct_answer_text = Q[i]['answers'][correct_answer_index]

    # ユーザーの答えと正解を比較
    if answ[i] == str(user_answer):
        print(f'<p>Question {i+1}: 正解！ 正解は {correct_answer_text} です。</p>')
    else:
        print(f'<p>Question {i+1}: 不正解。 正解は {correct_answer_text} です。</p>')

# 終了ボタンの追加
print('''
    <form action="your_finish_script.py">
        <input type="submit" value="終了" style="background-color: #ffff;">
    </form>
''')

print('</body></html>')

# 問題数

# 正答数