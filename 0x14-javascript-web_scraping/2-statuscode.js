#!/usr/bin/env node
// Write a script that display the status code of a GET request.
const request = require('request');
const url = process.argv[2];
const options = {
  url: url,
  method: 'GET'
};

request(options, (err, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${body.statusCode}`);
  }
});
