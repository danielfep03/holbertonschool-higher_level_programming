#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/';

request(url, (err, response, body) => {
  if (err) throw err;
  const characters = JSON.parse(body).characters;
  characters.forEach(element => {
    request(element, (err, response, body) => {
      if (err) throw err;
      const nameCharacter = JSON.parse(body).name;
      console.log(nameCharacter);
    });
  });
});
