const mysql = require('mysql2');
require('dotenv').config({ path: '.../.env' });

const db = mysql.createConnection({
    host: process.env.RDS_HOST, // RDS 엔드포인트
    user: process.env.USER_NAME, // RDS 사용자명
    password: process.env.USER_PASSWORD, // RDS 비밀번호
    database: process.env.DB_DATABASE
});

module.exports = db;