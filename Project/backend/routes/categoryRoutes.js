const express = require('express');
const router = express.Router();
const categoryController = require('../controllers/categoryController')

router.get('/subCategoryNavBar/:mainCategory', categoryController.subCategoryNavBar);
router.get('/showEntireItem/:mainCategory', categoryController.showEntireItem);
router.get('/showSubCategoryItem', categoryController.showSubCategoryItem);

module.exports = router;