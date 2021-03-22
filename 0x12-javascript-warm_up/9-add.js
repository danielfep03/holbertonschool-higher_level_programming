#!/usr/bin/node
const n1 = process.argv[2];
const n2 = process.argv[3];
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}

add(n1, n2);
