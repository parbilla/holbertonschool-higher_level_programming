#!/usr/bin/node
// Returns the reversed version of a list
exports.esrever = function (list) {
  const list1 = [];
  for (const i in list) {
    list1.unshift(list[i]);
  }
  return list1;
};
