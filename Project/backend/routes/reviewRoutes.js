const express = require('express');
const router = express.Router();
const reviewController = require('../controllers/reviewController')

router.get('/getReviewInfo/:itemId', reviewController.getReviewInfo);

module.exports = router;