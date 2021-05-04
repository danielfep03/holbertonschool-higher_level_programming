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
      const idCharacter = elem.split('/')[5];
      if (idCharacter === character) { count++; }
    });
  });
  console.log(count);
});
