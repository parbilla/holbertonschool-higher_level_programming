#!/usr/bin/node
// Imports an array and computes a new array
const list = require('./100-data').list;

const myList = list.map((x, i) => x * i);
console.log(list);
console.log(myList);
