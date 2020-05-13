#!/usr/bin/node
// Write a script that gets the contents of
// a webpage and stores it in a file
const request = require('request');
const fs = require('fs');
const file = process.argv[3];
const url = process.argv[2];
const options = {
  url: url,
  method: 'GET'
};
request(options, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(file, body, err => {
      if (err) {
        console.log(err);
      }
    });
  }
});
