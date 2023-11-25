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

exports.getSubCategoryProducts = (req, res) => {
    const subCategoryName = req.params.subCategoryName; // 클라이언트에서 전달한 서브카테고리 이름

    const query = `
    SELECT P.*, S.SubCategoryName
    FROM Product P
    INNER JOIN SubCategory S ON P.SubCategoryID = S.SubCategoryID
    WHERE S.SubCategoryName = ?
    `;

    db.query(query, [subCategoryName], (err, results) => {
        if (err) {
            console.error('Error fetching subcategory products:', err);
            res.status(500).json({ error: 'Error fetching subcategory products' });
            return;
        }

        res.json({ products: results });
    });
};

// 긍정 키워드를 가진 제품 정보 
exports.getProductsByPositiveKeyword = (req, res) => {
    const keyword = req.params.prosKeyword;
    const query = `
    SELECT P.*
    FROM Product P
    INNER JOIN ProductKeywords K ON P.ProductID = K.ProductID
    WHERE K.PositiveKeyword LIKE ?;`;

    db.query(query, [`%${keyword}%`], (err, results) => {
        if (err) {
            console.error('Error fetching product info by positive keyword:', err);
            res.status(500).json({ error: 'Error fetching product info by positive keyword' });
            return;
        }

        res.json({ products: results });
    });
};

// 부정 키워드를 가진 제품 정보 가져오기
exports.getProductsByNegativeKeyword = (req, res) => {
    const keyword = req.params.consKeyword; // 부정 키워드
    const query = `
    SELECT P.*
    FROM Product P
    INNER JOIN ProductKeywords K ON P.ProductID = K.ProductID
    WHERE K.NegativeKeyword LIKE ?;`;

    db.query(query, [`%${keyword}%`], (err, results) => {
        if (err) {
            console.error('Error fetching product info by negative keyword:', err);
            res.status(500).json({ error: 'Error fetching product info by negative keyword' });
            return;
        }

        res.json({ products: results });
    });
};