#!/usr/bin/env node

 // script that prints the first argument passed to it

 const myArgs = process.argv[2];
 if (myArgs === undefined) {
   console.log('No argument');
 } else {
   console.log(myArgs);
 }
