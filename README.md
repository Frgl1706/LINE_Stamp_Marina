#LINE Stamp Word Studio]

 マリナ-カメニ-レカーちゃんLINEスタンプに追加するワードを一緒に考えませんか。

LINEスタンプのフレーズ案やコメントを、リアルタイムでチーム・友人と共有しながらブラッシュアップできるインタラクティブWebアプリケーションです。スマホ・PC双方のレスポンシブ表示に対応し、9:16のキャンバス上でスタンプの見た目をリアルタイムに確認できます。

#主な機能
 * リアルタイムワード管理: 打ち込んだスタンプ候補フレーズを即座にリストへ同期・追加・削除。
 * 9:16 リアルタイムプレビュー: 背面の9:16イラスト上にスタンプテキストを表示し、視覚的な完成度をチェック。
 * 対話型コメントシステム:
   * 提案に対するコメント・返信・メンション機能。
   * 独自リアクションボタン（ いいね /  まりな！ /  わるいね）。
 * マルチデバイス対応: スマホとPCそれぞれの画面サイズに最適化されたレイアウト。
 * システム情報モーダル: 使い方、沿革、免責事項、言語設定などを集約。
🛠 技術スタック
 * フロントエンド: HTML5, CSS3 (Flexbox / CSS Grid / Responsive), JavaScript (ES6+)
 * バックエンド / データベース: Firebase Firestore (v10 Web SDK)

—————————————-

#導入手順
1. リポジトリのクローン
git clone https://github.com/your-username/line-stamp-word-studio.git
cd line-stamp-word-studio

2. Firebase の設定
 * Firebase Console で新規プロジェクトを作成し、Firestore Database を有効化します。
 * index.html 内の firebaseConfig を、自身のプロジェクト設定情報に置き換えてください。
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_PROJECT_ID.appspot.com",
  messagingSenderId: "YOUR_SENDER_ID",
  appId: "YOUR_APP_ID"
};

3. 実行
ローカルサーバー（Live Server等）を起動して index.html を開くか、GitHub Pages / Vercel / Firebase Hosting などの静的ホスティングサービスにデプロイして使用します。

——————————————

# 使い方
 * ユーザー名の設定: 画面右上のプロフィールエリアから名前を変更します。
 * ワードの投稿: 「スタンプのフレーズを入力」にテキストを入れて追加すると、リストと9:16キャンバスに即座に反映されます。
 * フィードバック: 「コメント」タブから提案に対して返信やリアクション（いいね・まりな！・わるいね）を投稿します。

——————————————

#ライセンス
MIT License



