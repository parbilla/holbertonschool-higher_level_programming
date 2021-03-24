#!/usr/bin/node
// Imports an array and computes a new array
const dict = require('./101-data').dict;
const myDict = {};
for (const key in dict) {
  if (myDict[dict[key]] === undefined) {
    myDict[dict[key]] = [key];
  } else {
    myDict[dict[key]].push(key);
  }
}
console.log(myDict);
