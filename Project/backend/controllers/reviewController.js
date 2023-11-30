const db = require('../config/rds')
const axios = require('axios');

exports.getReviewInfo = (req, res) => {
    const productId = req.params.itemId;

    // 리뷰
    const getReviewsQuery = `
        SELECT ReviewID, UserID, PositiveReviewText, NegativeReviewText, Rating
        FROM ProductReviews
        WHERE ProductID = ? ORDER BY UserId DESC;
    `;

    // 장단점
    const getProsConsQuery = `
        SELECT PositiveKeyword, PositiveRating, NegativeKeyword, NegativeRating
        FROM ProductKeywords
        WHERE ProductID = ?
    `;

    // 리뷰 개수
    const getReviewCountQuery = `
        SELECT COUNT(*) AS ReviewCount
        FROM ProductReviews
        WHERE ProductID = ?
    `;
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

exports.writeReview = async (req, res) => {
    const itemId = req.params.itemId;
    const userId = req.body.userId;
    const prosReview = req.body.prosReview;
    const consReview = req.body.consReview;
    const rating = req.body.rating;

    const insertReviewQuery = `
        INSERT INTO ProductReviews (ProductID, UserID, PositiveReviewText, NegativeReviewText, Rating)
        VALUES (?, ?, ?, ?, ?)
    `;

    try {
        // Assuming you have a 'db' connection configured somewhere in your code
        db.query(insertReviewQuery, [itemId, userId, prosReview, consReview, rating], async (err, results) => {
            if (err) {
                console.error('Error:', err);
                res.status(500).json({ error: 'Internal server error' });
            } else {
                // Check if the insertion was successful
                if (results.affectedRows > 0) {
                    // Respond to the original client request immediately
                    res.status(201).json({ message: '리뷰가 성공적으로 등록되었습니다!' });

                    // Fetch positive and negative keywords from the FastAPI endpoint
                    try {
                        const fastApiResponse = await axios.post(`http://0.0.0.0:1004/getJson/${itemId}`);
                        const { positiveKeywords, negativeKeywords } = fastApiResponse.data;

                        // Delete existing keywords for the given itemId
                        const deleteKeywordsQuery = `
                            DELETE FROM ProductKeywords
                            WHERE ProductID = ?
                        `;

                        db.query(deleteKeywordsQuery, [itemId], async (deleteErr, deleteResults) => {
                            if (deleteErr) {
                                console.error('Error deleting existing keywords:', deleteErr);
                                // Handle the error, you might want to log it or take other actions
                            } else {
                                // Insert positive and negative keywords into ProductKeywords table using a for loop
                                const insertKeywordQuery = `
                                    INSERT INTO ProductKeywords (ProductID, PositiveKeyword, PositiveRating, NegativeKeyword, NegativeRating)
                                    VALUES (?, ?, ?, ?, ?)
                                `;

                                for (let i = 0; i < positiveKeywords.length; i++) {
                                    const posKeyword = positiveKeywords[i];
                                    const negKeyword = negativeKeywords[i];
                                    db.query(insertKeywordQuery, [itemId, posKeyword.keyword, posKeyword.score, negKeyword.keyword, negKeyword.score]);
                                }
                            }
                        });
                    } catch (error) {
                        console.error('Error making FastAPI request:', error.message);
                        // Handle the error, you might want to log it or take other actions
                    }
                } else {
                    res.status(500).json({ error: '리뷰를 등록하는 중에 오류가 발생했습니다.' });
                }
            }
        });
    } catch (error) {
        console.error('Error:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
};



exports.getKeyword = (req, res) => {
    const productId = req.params.itemId;

    const GetProsInfo = `SELECT PositiveKeyWord, PositiveRating FROM ProductKeywords WHERE ProductID = ? ORDER BY PositiveRating DESC`;
    const GetConsInfo = `SELECT NegativeKeyWord, NegativeRating FROM ProductKeywords WHERE ProductID = ? ORDER BY NegativeRating DESC`;

    db.query(GetProsInfo, [productId], (err, prosResults) => {
        if (err) {
            console.error('Error fetching positive keywords:', err);
            res.status(500).json({ error: 'Error fetching positive keywords' });
            return;
        }
        db.query(GetConsInfo, [productId], (err, consResults) => {
            if (err) {
                console.error('Error fetching negative keywords:', err);
                res.status(500).json({ error: 'Error fetching negative keywords' });
                return;
            }
            res.json({
                Pros: prosResults,
                Cons: consResults
            });
        });
    });
};

exports.getConsKeyWordReviews = (req, res) => {
    const keyWord = req.query.keyWord;
    const itemId = req.query.itemId;
    const query = `
        select * from ProductReviews Where NegativeReviewText LIKE ? AND ProductID = ?;`;

    db.query(query, [`%${keyWord}%`, itemId], (err, results) => {
        if (err) {
            console.error('Error fetching product info by negative keyword:', err);
            res.status(500).json({ error: 'Error fetching product info by negative keyword' });
            return;
        }
        console.log(results);
        res.json({ results });
    });
};
