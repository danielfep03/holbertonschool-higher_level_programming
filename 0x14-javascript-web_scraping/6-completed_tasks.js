#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const taskDone = {};

request(url, 'utf-8', (err, response, body) => {
  if (err) throw err;
  const data = JSON.parse(body);
  data.forEach((element) => {
    if (element.completed === true) {
      if (taskDone[element.userId] === undefined) {
        taskDone[element.userId] = 1;
      } else {
        taskDone[element.userId]++;
      }
    }
  });
  console.log(taskDone);
});
