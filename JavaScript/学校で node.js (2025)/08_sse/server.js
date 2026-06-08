// 基本的なモジュールのインポート
import express from "express";
import path from "path";
import dotenv from "dotenv";
import { time } from "console";

// Express
const app = express();
// 環境変数の設定
dotenv.config();
const HOST = process.env.HOST || "localhost";
const PORT = process.env.PORT || 3000;
const __dirname = path.resolve();

// クライアント管理用変数
let clients = [];
// 現在の価格（シミュレート用）
let currentPrice = 100;
// SSE 用のインターバル管理変数
let stockInterval = null;

// TODO: 静的ファイルの提供 (publicフォルダ内の index.html 等)
app.use(express.static(path.join(__dirname, "public")));

// SSE エンドポイント: GET /stream
app.get("/stream", (req, res) => {
    // TODO: ヘッダー書き込み: writeHead() 200
    // Content-Type: text/event-stream
    // Cache-Control: no-cache
    // Connection: keep-alive
    res.writeHead(200, {
        "Content-Type": "text/event-stream",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
    });

    // クライアントを配列に追加
    clients.push(res);

    // ストリーミング開始
    startStreaming();

    // TODO: クライアント切断時の処理
    req.on("close", () => {
        // クライアントを配列から削除
        clients = clients.filter(client => client !== res);
        if (clients.length === 0) {
            // クライアントがいなくなったらインターバルを停止
            clearInterval(stockInterval);
            stockInterval = null;
        }
    });
});

app.listen(PORT, HOST, () => {
    console.log(`🚀 Server running at http://${HOST}:${PORT}`);
});

// ストリーミングロジック
const startStreaming = () => {
    if (stockInterval) return;
    // 1秒ごとに値をランダムに変動させてクライアントに送信
    stockInterval = setInterval(() => {
        // ランダムに価格を変動（シミュレート用データ）
        currentPrice = Math.max(0, currentPrice + (Math.random() - 0.5));
        // TODO: データの作成
        // type: "price"
        // time: 現在の時刻 (toLocaleTimeString)
        // value: currentPrice を小数点以下2桁でフォーマット
        const data = JSON.stringify({
            type: "price",
            time: new Date().toLocaleDateString(),
            value: currentPrice.toFixed(2),
        });

        // TODO: すべてのクライアントにデータを送信
        clients.forEach(res => res.write(`data: ${data}\n\n`));
    }, 1000);
};