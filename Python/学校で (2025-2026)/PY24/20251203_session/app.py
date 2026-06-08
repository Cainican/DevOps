# Session
#  一般的には、一連の通信の始まりから終わりまでを指す。
#  端的に言うとログイン状態の実現。
# [仕組み]
#  ①サーバーサイドにてセッションID(乱数)を生成し、
#   Cookieにてクライアントへ受け渡す。
#  ②クライアントは再リクエスト時に、セッションIDを渡す(Cookie)。
#  以上の流れから、サーバーサイドは、②のリクエストは①のユーザーであることが分かる。
# [情報の保存先]
#  セッション領域と呼ばれる、ユーザー専用のデータ保存領域があり、
#  サーバーサイドに保存される。
#  1つの例としては、セッションIDをファイル名として、
#  ユーザー専用のデータ保存領域を確保する。
#  サーバーサイドにデータが保存されるので、セキュリティが保たれる。
#  以上が一般的なセッションの仕組み。
#
#  Flaskのセッション
#  一般とは異なり、デフォルトのFlaskではサーバーサイドに情報を保持せず、
# "全てのセッション情報をCookieで管理"する。
# secure cookieと呼ばれ、SECRET_KEYで暗号化されて保存される。
# ※情報漏洩の危険性があるため、機密情報は保持しないこと。
# ※また、cookieのため、保存データ量の上限がある。
# ※Flask-Sessionという拡張ライブラリを用いれば、サーバーサイドに保存も可能となる。
from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = '85600317a65bbb753accff7a22deb929251dbd025622735f288a9b23f46f8ab0'
# py -c 'import secrets;print(secrets.token_hex())' # Flack officialより
# SECRET_KEYは、セッション情報暗号化のキー。セッション利用時はこの設定が必須。
# print(app.config) で、設定情報一覧が確認できる。

# セッションの有効期限変更
# ※既定は３１日
app.permanent_session_lifetime = timedelta(seconds=50)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/_session')
def _session():
  return redirect(url_for('index'))

@app.route('/start_session')
def start_session():
  # セッションの永続化
  # ※これを設定しないと、ブラウザを閉じたタイミングで
  # セッション領域が廃棄される。
  session.permanent = True
  session['id'] = 456
  return redirect(url_for('index'))

@app.route('/check_session')
def check_session():
  # セッションからデータを取得するには
  # session.get
  id = session.get('id')
  print(id)

  return redirect(url_for('index'))

@app.route('/end_session')
def end_session():
  # 個別削除にはsession.popを用いる
  session.pop('id', None)
  # 第二引数は、無い場合の既定値。
  # 第二引数が無く、キーが存在しない場合、
  # エラーとなるため、指定することが一般的。

  # セッション領域の全削除
  session.clear()

  return redirect(url_for('index'))

if __name__ == '__main__':
  app.run('0.0.0.0', 3000, True)