const express = require('express');
const router = express.Router();
const reviewController = require('../controllers/reviewController')

router.get('/getReviews', reviewController.getReviews);
router.get('/getProsCons', reviewController.getProsCons);