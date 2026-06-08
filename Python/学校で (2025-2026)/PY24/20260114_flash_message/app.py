# Flashメッセージ
#  1回だけ表示されるメッセージで、ページ更新がなされると消える。
#  簡単なメッセージを表示する用途で利用されている。
#  例）
#     ログイン画面で「IDまたはパスワードが違います。」とか、
#     登録画面で「登録が完了しました。」とか、
#     一覧画面で「削除しました。」とか。
#  内部的な仕組みてとしては、セッションを利用し、
#  PRGパターンと併用して用いることが一般的。
from flask import Flask, render_template, url_for, request, redirect, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = '85600317a65bbb753accff7a22deb929251dbd025622735f288a9b23f46f8ab0'


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/flash_message', methods = ['get', 'post'])
def flash_message():
  if request.method == 'GET':
    return render_template('flash_message.html')
  else:
    flash('一度だけ表示。')
    flash('複数メッセージOK。')
    return redirect(url_for('flash_message'))

@app.route('/flash_category', methods = ['get', 'post'])
def flash_category():
  if request.method == 'GET':
    return render_template('flash_category.html')
  else:
    flash('一度だけ表示。') # 既定はmessage
    flash('複数メッセージOK。', 'success')
    flash('エラー', 'danger')
    # カテゴリーは自由に命名できるが、以下の４つが一般的。
      # ・success(成功)
      # ・info(情報/通知)
      # ・warning(警告)
      # ・danger/error(エラー)
      # ※dangerはBootstrap利用時に用いられる。
    return redirect(url_for('flash_category'))

if __name__ == '__main__':
  app.run('0.0.0.0', 3000, True)