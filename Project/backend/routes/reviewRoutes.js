const express = require('express');
const router = express.Router();
const reviewController = require('../controllers/reviewController')

router.get('/getReviewInfo/:itemId', reviewController.getReviewInfo);
router.post('/writeReview/:itemId', reviewController.writeReview);
router.get('/getKeyword/:itemId', reviewController.getKeyword);
router.get('/getConsKeyWordReviews', reviewController.getConsKeyWordReviews);
module.exports = router;