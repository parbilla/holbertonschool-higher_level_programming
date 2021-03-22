#!/usr/bin/node
function factorial (n) {
  if (isNaN(n) === true || (n === 1)) {
    return 1;
  } else {
    return (n * factorial(n - 1));
  }
}
const factor = parseInt(process.argv[2]);
console.log(factorial(factor));
