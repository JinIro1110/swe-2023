const db = require('../config/db');

// 제품 리뷰 가져오기
exports.getReviews = (req, res) => {
    const productID = req.params.productID;

    const query = `
    SELECT *
    FROM ProductReviews
    WHERE ProductID = ?
    `;

    db.query(query, [productID], (err, results) => {
        if (err) {
            console.error('Error fetching product reviews:', err);
            res.status(500).json({ error: 'Error fetching product reviews' });
            return;
        }

        res.json({ productReviews: results });
    });
};

// 제품 장점, 단점 가져오기
exports.getProsCons = (req, res) => {
    const productID = req.params.productID;

    const query = `
    SELECT PositiveKeyword, PositiveRating, NegativeKeyword, NegativeRating
    FROM ProductKeywords
    WHERE ProductID = ?
    `;

    db.query(query, [productID], (err, results) => {
        if (err) {
            console.error('Error fetching product advantages and disadvantages:', err);
            res.status(500).json({ error: 'Error fetching product advantages and disadvantages' });
            return;
        }

        res.json({ productKeywords: results });
    });
};