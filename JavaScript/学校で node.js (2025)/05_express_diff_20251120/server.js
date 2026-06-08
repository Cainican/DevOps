// dotenv インポート(ESM)
import dotenv from 'dotenv';
// express インポート(ESM)
import express from 'express';
// path モジュールのインポート
import path from 'path';

// Dotenvの設定をロード
dotenv.config();

// モデルのインポート
import { fetchProducts, findProductById, searchProducts } from './models/Product.js';

// 環境変数の取得（デフォルト値も設定）
const HOST = process.env.HOST || 'localhost';
const PORT = process.env.PORT || 3000;
const BASE_URL = `http://${HOST}:${PORT}/`

console.log(BASE_URL);

// 現在のディレクトリパスを取得
const __dirname = path.resolve();
console.log(__dirname);

// Expressアプリケーションの初期化
const app = express();

// ミドルウェア設定
// app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(__dirname + '/public'));

// リクエストログ用ミドルウェア
app.use((req, res, next) => {
    console.log(`ミドルウェア: ${req.method} ${req.url}`);
    // 次の処理へ
    next();
});

// カート情報 (メモリ上)
let cartItems = [];

// ------------------------
// ページルーティング
// ------------------------
// GET: エンドポイント: /test
app.get('/test', (req, res) => {
    console.log("ルーティング: /test");
    const message = 'Hello, Express!';
    res.send(message);
});

// GET: エンドポイント: /test
app.get('/info', (req, res) => {
    console.log("ルーティング: /info");
    const message = 'Hello, Express!';
    res.send(message);
});

// POST: エンドポイント: /save
app.post('/save', (req, res) => {
    console.log("ルーティング: /save");
    const message = 'POST リクエストを受け取りました';

    res.send(message);
});

// GET: エンドポイント: /
app.get('/', (req, res) => {
    console.log("ルーティング: /");
    const path = __dirname + '/public/home.html';
    res.sendFile(path);
});

// GET: エンドポイント: /search : keyword クエリパラメータ対応
app.get('/search', (req, res) => {
    console.log("ルーティング: /search");
    if (req.query.keyword) {
        const keyword = req.query.keyword;
        console.log("検索キーワード: " + keyword);
    }
    const path = __dirname + '/public/home.html';
    res.sendFile(path);
});

// GET: エンドポイント: /about
app.get('/about', (req, res) => {
    console.log("ルーティング: /about");
    const path = __dirname + '/public/about.html';
    res.sendFile(path);
});

// GET: エンドポイント: /product/:id
app.get('/product/:id', (req, res) => {
    const id = req.params.id;
    console.log("ルーティング: /product/" + id);
    const path = __dirname + '/public/product.html';
    res.sendFile(path);
});

// ------------------------
// API ルーティング
// ------------------------
// GET: エンドポイント: /api/product/list
app.get('/api/product/list', (req, res) => {
    console.log("ルーティング: /api/product/list");

    // 商品データを取得
    const products = fetchProducts();

    // JSON データを返す
    const data = { products }
    res.json(data);
});

// GET: エンドポイント: /api/product/show/:id
app.get('/api/product/show/:id', (req, res) => {
    const id = Number(req.params.id);
    console.log(`ルーティング: /api/product/show/${id}`);

    // 商品データを取得
    const product = findProductById(id);

    // JSON データを返す
    res.json(product);
});

// GET: エンドポイント: /api/search : keyword クエリパラメータ対応
app.get('/api/search', (req, res) => {
    console.log("ルーティング: api/search");

    const keyword = req.query.keyword || '';
    const products = searchProducts(keyword);

    // JSON データを返す
    const data = { products }
    res.json(data);
});

// ------------------------
// Express 起動
// ------------------------
app.listen(PORT, HOST, () => {
    console.log(`Server running: ${BASE_URL}`);
});