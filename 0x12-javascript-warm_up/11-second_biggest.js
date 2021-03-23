#!/usr/bin/node
let second = 0;
const args = process.argv.slice(2);
if (args.length > 1) {
  args.sort(function (a, b) { return a - b; });
  second = args[args.length - 2];
}
console.log(second);
