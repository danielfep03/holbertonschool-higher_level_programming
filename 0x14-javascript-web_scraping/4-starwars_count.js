#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let count = 0;
const character = '18';

request(url, (err, response, body) => {
  const results = JSON.parse(body).results;
  if (err) throw err;
  results.forEach(element => {
    element.characters.forEach(elem => {
      console.log(elem.split('/'));

      if (elem === character) { count++; }
    });
  });
  console.log(count);
});
