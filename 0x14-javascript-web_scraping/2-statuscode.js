#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, response) => {
  if (err) throw err;
  console.error(`code: ${response.statusCode}`);
});
