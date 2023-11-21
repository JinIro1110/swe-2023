const db = require('../config/db');

// 아이템 클릭 시 아이템들에 대한 정보 가져오기
exports.getProductInfo = (req, res) => {
    const productId = req.params.itemId;
    const query = `
    SELECT P.*, S.SubCategoryName
    FROM Product P
    INNER JOIN SubCategory S ON P.SubCategoryID = S.SubCategoryID
    WHERE P.ProductID = ?
    `;

    db.query(query, [productId], (err, results) => {
        if (err) {
            console.error('Error fetching product info:', err);
            res.status(500).json({ error: 'Error fetching product info' });
            return;
        }

        if (results.length === 0) {
            res.status(404).json({ error: 'Product not found' });
            return;
        }

        const productInfo = results[0];
        res.json({ productInfo });
    });
};

exports.getProductRating = (req, res) => {
    const productId = req.params.itemId;
    const query = `
    SELECT Rating
    FROM Product
    WHERE ProductID = ?
    `;

    db.query(query, [productId], (err, results) => {
        if (err) {
            console.error('Error fetching product rating:', err);
            res.status(500).json({ error: 'Error fetching product rating' });
            return;
        }

        if (results.length === 0) {
            res.status(404).json({ error: 'Product not found' });
            return;
        }

        const rating = results[0].Rating;
        res.json({ rating });
    });
};