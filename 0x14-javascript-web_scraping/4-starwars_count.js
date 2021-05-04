#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let count = 0;
const character = 'https://swapi-api.hbtn.io/api/people/18/';

request(url, (err, response, body) => {
  if (err) throw err;
  const results = JSON.parse(body).results;
  results.forEach(element => {
    element.characters.forEach(elem => {
      if (elem === character) { count++; }
    });
  });
  console.log(count);
});
