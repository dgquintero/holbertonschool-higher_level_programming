#!/usr/bin/node

const myArgs = process.argv.slice(2);
let secondMax = 0;
if (myArgs.length > 1) {
  myArgs.sort();
  secondMax = myArgs[myArgs.length - 2];
}
console.log(secondMax);
