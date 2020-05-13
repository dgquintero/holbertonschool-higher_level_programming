#!/usr/bin/env node
// Write a script that writes a string to a file.
const fs = require('fs');
const data = process.argv[3];
const file = process.argv[2];
fs.writeFile(file, data, err => {
  if (err) {
    console.log(err);
  }
  console.log(data);
});
