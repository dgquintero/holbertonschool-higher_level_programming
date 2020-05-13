#!/usr/bin/env node
// Write a script that computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];
const options = {
  url: url,
  method: 'GET'
};

request(options, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const dicUser = {};
    for (const users of data) {
      if (users.completed) {
        if (dicUser[users.userId]) {
          dicUser[users.userId] += 1;
        } else {
          dicUser[users.userId] = 1;
        }
      }
    }
    console.log(dicUser);
  }
});
