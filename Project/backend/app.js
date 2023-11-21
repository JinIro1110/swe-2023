const express = require('express');
const app = express();
require('dotenv').config({ path: '../.env' });
const categoryRoutes = require('./routes/categoryRoutes')
const itemRoutes = require('./routes/itemRoutes')
const reviewRoutes = require('./routes/reviewRoutes')
// const rds = require('./config/rds')
const db = require('./config/db')

// app.use('/category', categoryRoutes);
// app.use('/item', itemRoutes);
// app.use('/reviewRoutes', reviewRoutes);

app.get('/', (req, res) => {
    const query = `
    SELECT SubCategoryName
    FROM SubCategory
    INNER JOIN MainCategory ON MainCategory.CategoryID = SubCategory.CategoryID
    WHERE MainCategory.CategoryName = '간식'
    `;

    db.query(query, (err, results) => {
        if (err) {
            console.error('Error fetching subcategories:', err);
            res.status(500).json({ error: 'Error fetching subcategories' });
            return;
        }

        // 결과를 클라이언트에 전달
        res.json({ subcategories: results });
    });
});

const PORT = process.env.PORT || 3000;


app.listen(PORT, () => {
    console.log(`서버가 포트 ${PORT}에서 실행 중입니다.`);
});
