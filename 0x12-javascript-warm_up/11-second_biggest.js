#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (myArgs.length < 2) {
  console.log(0);
  return;
}
myArgs.sort();
const secondMax = myArgs[myArgs.length - 2];
console.log(secondMax);
