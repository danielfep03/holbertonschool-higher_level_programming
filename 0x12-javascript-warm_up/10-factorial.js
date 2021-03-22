#!/usr/bin/node
const number = process.argv[2];
function factorialRecursivo (n) {
  if (n === 0) {
    return 1;
  }
  return n * factorialRecursivo(n - 1);
}
if (!isNaN(number)) { console.log(factorialRecursivo(process.argv[2])); } else {
  console.log(1);
}
