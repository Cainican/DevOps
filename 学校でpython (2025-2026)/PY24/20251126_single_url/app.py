# Flaskでは、同一エンドピントに、
# 以下の様に構成するのが代表的。
#   ・GET
#   ・POSTの場合...
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# methodsでGET, POSTの両方を受け付ける。
@app.route('/', methods=['get', 'post'])
def index():
  # requist.methodで、GETとPOSTの
  # 処理を切る分けることができる。
  if request.method == 'GET': # ここは大文字限定
    return render_template('index.html')
  else:
    id = request.form.get('id')

    # 入力チェック
    if not id:
      # NGなら自ページにリダイレクト
      return redirect(url_for('index'))

    # 入力チェックOKならDB登録etc...
    # その後、リダイレクト。
    # リダイレクト先としては、以下２つか一般的
    # ・自ページ
    # ・完了ページ

    # 確認画面を設ける場合も、リダイレクトにて実装
    # ❈要Session

    return '登録完了'

if __name__ == '__main__':
  app.run('0.0.0.0', 3000, True)