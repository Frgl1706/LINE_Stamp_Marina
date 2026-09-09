from flask import Flask, request, jsonify
import csv
import os
import time

app = Flask(__name__, static_folder='.', static_url_path='')

CSV_FILE = 'data.csv'

# CSVファイルが存在しない場合は初期化（ヘッダー作成）
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'type', 'text', 'user', 'timestamp', 'parent_id', 'reaction'])

@app.route('/')
def index():
    return app.send_static_file('index.html')

# データを全件取得するAPI
@app.route('/api/data', methods=['GET'])
def get_data():
    data = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
    return jsonify(data)

# データを追加するAPI
@app.route('/api/add', methods=['POST'])
def add_data():
    req = request.json
    new_row = [
        str(int(time.time() * 1000)),  # id (タイムスタンプ)
        req.get('type', 'word'),       # type: 'word' or 'comment'
        req.get('text', ''),           # テキスト内容
        req.get('user', '名無し'),      # ユーザー名
        time.strftime('%Y-%m-%d %H:%M:%S'), # 投稿日時
        req.get('parent_id', ''),      # 返信先のID（ワードのIDなど）
        req.get('reaction', '')        # リアクションの種類
    ]
    
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(new_row)
        
    return jsonify({"status": "success", "data": new_row})

if __name__ == '__main__':
    print("サーバーを起動しました: http://127.0.0.1:8000")
    app.run(port=8000, debug=True)
Z
