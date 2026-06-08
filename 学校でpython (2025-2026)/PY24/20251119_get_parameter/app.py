from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/next')
def next():
  # クエリパラメータを取得するには、
  # request.argsを用いる。

  # 単一値の取得
  # 方法その1
  id = request.args.get('id')

  # 取得できなければNone
  id = request.args.get('id2')
  if id is None:
    id = 'None'

  # Noneの場合の既定値設定可能
  id = request.args.get('id2', default='none')

  # ちゃんとしたチェック処理を作ってみると。。。
  id = request.args.get('id')
  if not id:
    return 'IDは必須'

  # 方法その２
  id = request.args['id']

  # こっちの場合、取得できない場合はエラーとなる。
  # id = request.args['id2']

  # 連数値
  names = request.args.getlist('names')
  names = request.args.getlist('names2')
  # 取得できない場合は空のリスト

  # 空テック
  if not names:
    names = ['空']

  return id + ''.join(names)

if __name__ == '__main__':
  app.run('0.0.0.0', 3000, True)