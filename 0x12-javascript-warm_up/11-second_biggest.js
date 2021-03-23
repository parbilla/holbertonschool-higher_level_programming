#!/usr/bin/node
let args = process.argv.slice(2);
let second = 0;
if (args.length > 1) {
    args.sort();
    second = args[args.length - 2];
}
console.log(second);
