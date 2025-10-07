const fs = require('fs');
const express = require('express');
const cors = require('cors');
const app = express();

// 讓前端可以送 JSON
app.use(express.json());
app.use(cors());

// 設定 JSON 檔路徑（放在 wwwroot 裡）
const filePath = "C:/inetpub/wwwroot/drawing_progress.json";

// 提供讀取 JSON API
app.get('/progress', (req, res) => {
  if (fs.existsSync(filePath)) {
    const data = fs.readFileSync(filePath, 'utf8');
    res.json(JSON.parse(data));
  } else {
    res.json({ completed: 0, total: 100 });
  }
});

// 提供更新 JSON API
app.post('/update-progress', (req, res) => {
  const data = req.body;
  fs.writeFileSync(filePath, JSON.stringify(data, null, 2));
  res.json({ status: 'ok', saved: data });
});

// 啟動伺服器
app.listen(3000, () => console.log("後台 API 已啟動 → http://localhost:3000"));
