#!/usr/bin/env node

 // Write a script that prints My number: <first argument converted in integer

 const myArgs = process.argv[2];
 console.log(typeof (myArgs));
 console.log(typeof (~~myArgs));
