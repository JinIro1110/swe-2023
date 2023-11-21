const mysql = require('mysql2');

const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'abcd1234!@#$',
    database: 'beluv'
});

module.exports = db;