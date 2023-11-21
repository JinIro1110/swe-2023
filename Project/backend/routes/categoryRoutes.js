const express = require('express');
const router = express.Router();
const categoryController = require('../controllers/categoryController')

router.get('/subCategoryNavBar', categoryController.subCategoryNavBar);
router.get('/showEntireItem', categoryController.showEntireItem);
router.get('/showSubCategoryItem', categoryController.showSubCategoryItem);