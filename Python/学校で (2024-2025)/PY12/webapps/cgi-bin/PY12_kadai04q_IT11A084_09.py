############################################
#   Kadai04q-IT11A084-09 エリアッセンカスパ  #
############################################

# import the necessary tools
# 文字化け対策
import sys
import io
import cgi
import random

# 出力のエンコーディングを設定
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='UTF-8')

# ヘッダーの設定
print("Content-Type: text/html; charset=UTF-8")
print("")

# デバッグ用にエラーメッセージを表示
import cgitb
cgitb.enable()

# 問題のリスト
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

def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='UTF-8')

    # 問題をランダムにシャッフル
    random.shuffle(Q)

    # 正解の答えをカンマ区切りの文字列で取得
    num = [str(i['correct']) for i in Q]
    connect = ','.join(num)

    # HTML出力
    print(f'''
    <html>
        <meta charset="UTF-8">
        <head><title>課題4 フォムコントロール</title></head>
        <body style="background-color: #99ffff">

            <p>IT11A084-09-エリアッセン カスパ</p>

            <form action="PY12-kadai04a-IT11A084-09.py">
                <input type="hidden" name="c" value="{connect}">
    ''')

    # ランダムに並び替えた質問を表示
    for i in range(len(Q)):
        print(f'<h3>{Q[i]["question"]}</h3>')

        # 各質問の選択肢を表示
        for j in range(len(Q[i]['answers'])):
            print(f'<input type="radio" name="q{i}" value="{j}" id="{i}{j}"> <label for="{i}{j}">{Q[i]["answers"][j]}</label><br>')

    # 送信ボタンを表示
    print('''
                <input type="submit" value="回答">
            </form>
        </body>
    </html>
    ''')

# メイン処理を実行
main()






#<h3>日本人の体温平均は36度ですが、グリーンランド人の体温平均は何度でしょうか?</h3>
#                <input type="radio" name="ans" value="ア">36度<br></input>
#               <input type="radio" name="ans" value="イ">35.7度<br></input>
#                <input type="radio" name="ans" value="ウ">37度<br></input>
#                <input type="radio" name="ans" value="エ">36.3度<br></input>
#                <input type="submit" value="回答">
#              </form>
#
#            </body>
#          </html>