from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

# postを受け取るには、methodsの指定が必須
@app.route('/confirm', methods=['post'])
def confirm():
  # Formデータを取得するには、
  # request.argsを用いる。
  # ❈全船request.argsと一緒。

  # フォームデータ (単一値) の取得
  id = request.form.get('id')

  # 必須テック
  if not id:
    return 'IDは必須' # 本来はリダイレクト
  
  # フォームデータ (単一値) の取得
  check = request.form.get('check')

  # 必須テック
  if not check:
    pass
    # エラーとする場合にはエラー処理

  return render_template('confirm.html')

if __name__ == '__main__':
  app.run('0.0.0.0', 3000, True)