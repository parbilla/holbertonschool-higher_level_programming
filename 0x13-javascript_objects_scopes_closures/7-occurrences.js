#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let cont = 0;
  for (let i = 0; i < list.length; i++) {
    (list[i] === searchElement ? cont++ : cont);
  }
  return cont;
};
