#!/usr/bin/node

/* script that prints x times “C is fun” */

const myVar = 'C is fun';
let i = 0;
for (; i < process.argv[2]; i++) {
  console.log(myVar);
}
