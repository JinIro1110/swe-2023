const express = require('express');
const app = express();
require('dotenv').config({ path: '../.env' });
const db = require('./config/db')

const PORT = process.env.PORT || 3000;
app.get('/', (req, res) => {
    db.query('SELECT * FROM ProductReviews', (err, results) => {
        if (err) {
            console.error(err);
            res.status(500).send('내부 서버 오류');
        } else {
            console.log(results);
        }
    });
});

app.listen(PORT, () => {
    console.log(`서버가 포트 ${PORT}에서 실행 중입니다.`);
});
