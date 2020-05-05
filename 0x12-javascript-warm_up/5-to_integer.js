#!/usr/bin/node

 // Write a script that prints My number: <first argument converted in integer

const myArgs = process.argv[2];
if (isNaN(myArgs)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myArgs);
}
