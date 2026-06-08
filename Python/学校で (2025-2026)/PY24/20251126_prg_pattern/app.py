# PRGパターン
# POST Redirect Get pattern
# Postのままだと、更新時に不具合を起こすから
# Redirectして、POST要求からGET要求に
# 変更する手法
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/products/new')
def products_new():
  return render_template('products/new.html')

@app.route('/products', methods=['post'])
def products():
  id = request.form.get('id')
  # 入力値チェック 割愛

  # DB登録割愛
  import datetime
  print(datetime.datetime.now())

  return render_template('products/create_complete.html')


@app.route('/products_prg/new')
def products_prg_new():
  return render_template('products_prg/new.html')

@app.route('/products_prg', methods=['post'])
def products_prg():
  id = request.form.get('id')
  # 入力値チェック 割愛

  # DB登録割愛
  import datetime
  print(datetime.datetime.now())

  # return render_template('products/create_complete.html')
  # リダイレクトして、POST要求をGET要求に変える
  return redirect(url_for('pcc'))

@app.route('/pcc')
def pcc():
  return render_template('products/create_complete.html')

if __name__ == '__main__':
  app.run('0.0.0.0', 3000, True)