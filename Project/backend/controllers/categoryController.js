const db = require('../config/rds')

// 서브 카테고리 네비바 생성
exports.subCategoryNavBar = (req, res) => {
    const mainCategoryName = req.params.mainCategory;
    const query = `
    SELECT SubCategoryName
    FROM SubCategory
    INNER JOIN MainCategory ON MainCategory.CategoryID = SubCategory.CategoryID
    WHERE MainCategory.CategoryName = ?
    `;

    db.query(query, [mainCategoryName], (err, results) => {
        if (err) {
            console.error('Error fetching subcategories:', err);
            res.status(500).json({ error: 'Error fetching subcategories' });
            return;
        }
        res.json({ subcategories: results });
    });
};

// 아이템 진열(카테고리 전체 클릭시 전체 아이템)
exports.showEntireItem = (req, res) => {
    const categoryName = decodeURIComponent(req.params.mainCategory);
    const query = `
    SELECT distinct *
    FROM MainCategory
    INNER JOIN SubCategory ON MainCategory.CategoryID = SubCategory.CategoryID
    INNER JOIN Product ON SubCategory.SubCategoryID = Product.SubCategoryID
    WHERE MainCategory.CategoryName = ?
    `;

    db.query(query, [categoryName], (err, results) => {
        if (err) {
            console.error('Error fetching data:', err);
            res.status(500).json({ error: 'Error fetching data' });
            return;
        }
        res.json({ mainCategoryItems: results });
    });
};

// 네비바 클릭시 소 카테고리 아이템 보여주기
exports.showSubCategoryItem = (req, res) => {
    const subcategoryName = decodeURIComponent(req.params.subCategory);
    console.log(this.subCategoryName);
    const query = `
    SELECT *
    FROM Product
    INNER JOIN SubCategory ON SubCategory.SubCategoryID = Product.SubCategoryID
    WHERE SubCategory.SubCategoryName = ?
    `;

    db.query(query, [subcategoryName], (err, results) => {
        if (err) {
            console.error('Error fetching items:', err);
            res.status(500).json({ error: 'Error fetching items' });
            return;
        }

        res.json({ subCategoryItems: results });
    });
};
