#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const taskDone = {};
let lastId = 1;
let acum = 0;

request(url, (err, response, body) => {
  if (err) throw err;
  const data = JSON.parse(body);
  data.forEach((element) => {
    if (element.completed === true) {
      if (element.userId !== lastId) {
        acum = 0;
        lastId = element.userId;
      }
      taskDone[element.userId] = ++acum;
    }
  });
  console.log(taskDone);
});
