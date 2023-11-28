const express = require('express');
const app = express();
require('dotenv').config({ path: '../.env' });
const cors = require('cors')
const categoryRoutes = require('./routes/categoryRoutes')
const itemRoutes = require('./routes/itemRoutes')
const reviewRoutes = require('./routes/reviewRoutes')
const rds = require('./config/rds')


app.use(cors());
app.use(express.json());
app.use('/api/category', categoryRoutes);
app.use('/api/item', itemRoutes);
app.use('/api/review', reviewRoutes);

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
    console.log(`서버가 포트 ${PORT}에서 실행 중입니다.`);
});
