#!/usr/bin/node
const fs = require('fs');
const data = fs.readFileSync(process.argv[2], 'utf8');
const data2 = fs.readFileSync(process.argv[3], 'utf8');
const fileA = data;
const fileB = data2;

const text = fileA + fileB;
fs.appendFile(process.argv[4], text, function () {});
