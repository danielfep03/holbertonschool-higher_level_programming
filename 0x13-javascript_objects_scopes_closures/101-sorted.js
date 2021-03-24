#!/usr/bin/node
const obj = require('./101-data');
const object = obj.dict;
const newObject = {};
const array = Object.values(object);

for (let i = 0; i < array.length; i++) {
  newObject[array[i]] = [];
}

for (const i in object) {
  for (let j = 0; j < array.length; j++) {
    if (object[i] === array[j]) {
      (newObject[array[j]]).push(i);
      break;
    }
  }
}

console.log(newObject)
;
