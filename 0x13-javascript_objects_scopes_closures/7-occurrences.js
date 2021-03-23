#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((acum, element) => element === searchElement ? acum + 1 : acum, 0);
};
