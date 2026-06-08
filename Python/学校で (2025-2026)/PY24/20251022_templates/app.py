# MVTモデル
#  M(Model)…業務ロジックを担当
#  V(View)…入力を受け取り、ModelとTemplateの制御を担当
#  T(Template)…入出力画面を担当
# ちなみに、当ファイルはVになる。
# おまけ。MVCと対応すると、V=C, T=Vになる。

# テンプレートエンジン
#  HTMLを中心に、動的なページを作成する仕組み。
#  Flaskでは、Jinja2というテンプレートエンジンを利用。
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  # HTMLファイルを読み込んで、返却。
  return render_template('index.html')

  # テンプレートファイル(html)は、
  # 「templates」フォルダに配置する
  # 必要がある

# ViewからTemplateにデータを引き渡す
@app.route('/pass_data')
def pass_data():
  # 第２引数以降に、キーワード引数で」受け渡す
  return render_template('pass_data.html', id = 123, name = '<h1>abc</h1>')

# if for
@app.route('/if_for')
def if_for():
  age = 20
  colors = ['r', 'g', 'b']
  colors_dic = {
    'r': '赤',
    'g': '緑',
    'b': '青'
  }

  from user import User
  users = [User(1, 'a'), User(2, 'b'), User(3, 'c')]
  return render_template('if_for.html', age = age, colors = colors, colors_dic = colors_dic, users = users)

# 画像/css/js
@app.route('/img_etc')
def img_etc():
  return render_template('img_etc.html')

# コンポーネント
@app.route('/component')
def component():
  return render_template('component.html')

# レイアウト継承
@app.route('/extends')
def extends():
  return render_template('extends.html')

# フィルター
@app.route('/filter')
def filter():
  age = 20
  colors = ['r', 'g', 'b']
  return render_template('filter.html', age = age, colors = colors)

# その他
@app.route('/other')
def other():
  age = 20
  colors = ['r', 'g', 'b']
  return render_template('other.html', age = age, colors = colors)

if __name__ == '__main__':
  app.run('0.0.0.0', 5000, True)