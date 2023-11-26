const express = require('express');
const router = express.Router();
const itemController = require('../controllers/itemController');

router.get('/getProductInfo/:itemId', itemController.getProductInfo);
router.get('/getProductRating/:itemId', itemController.getProductRating);
router.get('/getSameProsProduct', itemController.getSameProsProduct);
module.exports = router;