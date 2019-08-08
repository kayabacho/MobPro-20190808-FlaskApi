# 必要なモジュールの読み込み
from flask import Flask, jsonify, abort, make_response
import random

# Flaskクラスのインスタンスを作成
# __name__は現在のファイルのモジュール名
api = Flask(__name__)

#ランダムで生成する
def createJanken():
    random.seed()
    return random.choice(['per','choki','goo'])

# GETの実装
@api.route('/janken', methods=['GET'])
def get():
    # result = { "greeting": 'hello flask' }
    result = { 'janken': createJanken() }
    return make_response(jsonify(result))

# エラーハンドリング
@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# ファイルをスクリプトとして実行した際に
# ホスト0.0.0.0, ポート3001番でサーバーを起動
if __name__ == '__main__':
    api.run(host='127.0.0.1', port=3001)
