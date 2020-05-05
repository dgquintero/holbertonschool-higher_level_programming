#!/usr/bin/node
/* script that prints “Javascript is amazing” */
const num = process.argv[2];
function factorial(num) {
  if (isNaN(num) || num === 1) {
    return 1;
  }
  return (num * factorial(num - 1));
}
console.log(factorial(parseInt(num)));
