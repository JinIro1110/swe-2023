const db = require('../config/db');

exports.getReviewInfo = (req, res) => {
    const productId = req.params.itemId;

    // 리뷰 정보 가져오기
    const getReviewsQuery = `
        SELECT ReviewID, PositiveReviewText, NegativeReviewText, Rating
        FROM ProductReviews
        WHERE ProductID = ?
    `;

    // 장단점 정보 가져오기
    const getProsConsQuery = `
        SELECT PositiveKeyword, PositiveRating, NegativeKeyword, NegativeRating
        FROM ProductKeywords
        WHERE ProductID = ?
    `;

    // 리뷰 개수 가져오기
    const getReviewCountQuery = `
        SELECT COUNT(*) AS ReviewCount
        FROM ProductReviews
        WHERE ProductID = ?
    `;

    // 여러 쿼리를 병렬로 실행
    db.query(getReviewsQuery, [productId], (err, reviewsResults) => {
        if (err) {
            console.error('Error fetching product reviews:', err);
            res.status(500).json({ error: 'Error fetching product reviews' });
            return;
        }

        db.query(getProsConsQuery, [productId], (err, prosConsResults) => {
            if (err) {
                console.error('Error fetching product advantages and disadvantages:', err);
                res.status(500).json({ error: 'Error fetching product advantages and disadvantages' });
                return;
            }

            db.query(getReviewCountQuery, [productId], (err, reviewCountResults) => {
                if (err) {
                    console.error('Error fetching product review count:', err);
                    res.status(500).json({ error: 'Error fetching product review count' });
                    return;
                }

                if (reviewsResults.length === 0) {
                    res.status(404).json({ error: 'No reviews found for the product' });
                    return;
                }

                const reviewInfo = {
                    productReviews: reviewsResults,
                    productProsCons: prosConsResults,
                    reviewCount: reviewCountResults[0].ReviewCount,
                };

                res.json({ reviewInfo });
            });
        });
    });
};
