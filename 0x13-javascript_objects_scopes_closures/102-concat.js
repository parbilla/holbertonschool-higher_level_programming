#!/usr/bin/node
// Script that concats 2 files
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
const fs = require('fs');
const textA = fs.readFileSync(fileA, { encoding: 'utf8', flag: 'r' });
const textB = fs.readFileSync(fileB, { encoding: 'utf8', flag: 'r' });
fs.writeFileSync(fileC, textA + textB);
