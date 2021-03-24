#!/usr/bin/node
const fs = require('fs');
let fileA;
let fileB;
try {
  const data = fs.readFileSync(process.argv[2], 'utf8');
  const data2 = fs.readFileSync(process.argv[3], 'utf8');
  fileA = data;
  fileB = data2;
} catch (err) {
  console.error(err);
}

const text = fileA + fileB;
fs.appendFile(process.argv[4], text, (err) => {
  if (err) throw err;
  console.log('The "data to append" was appended to file!');
});
