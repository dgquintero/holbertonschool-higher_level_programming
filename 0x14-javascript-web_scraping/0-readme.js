#!/usr/bin/env node
// Write a script that reads and prints the content of a file
const myArg = process.argv[2];
const fs = require('fs');

fs.readFile(myArg, 'utf-8', (err, data) => {
    if(err) {
        throw err;
    }
    console.log(data);
});
