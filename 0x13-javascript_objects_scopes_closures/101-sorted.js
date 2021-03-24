#!/usr/bin/node
const obj = require('./101-data');
const object = obj.dict;
const new_object = {};
const array = Object.values(object);

for (let i = 0; i < array.length; i++) {
  new_object[array[i]] = [];
}

for (const i in object) {
  for (let j = 0; j < array.length; j++) {
    if (object[i] === array[j]) {
      (new_object[array[j]]).push(i);
      break;
    }
  }
}

console.log(new_object)
;
