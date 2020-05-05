#!/usr/bin/node

// script that prints a square
const myVar = 'X';
const myArgs = process.argv[2];
let i = 0;
if (isNaN(myArgs)) {
  console.log('Missing size');
} else {
  for (; i < process.argv[2]; i++) {
    console.log(myVar.repeat(myArgs));
  }
}
