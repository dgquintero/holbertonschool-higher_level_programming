#!/usr/bin/node
// script that searches the second biggest integer in the list
let secondMax = 0;
const myArgs = process.argv.slice(2);
if (myArgs.length > 1) {
  myArgs.sort();
  secondMax = myArgs[myArgs.length - 2];
}
console.log(secondMax);
