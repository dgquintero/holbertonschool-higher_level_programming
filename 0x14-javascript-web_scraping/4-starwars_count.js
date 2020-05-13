#!/usr/bin/node
// Write a script that prints the number of movies
// where the character “Wedge Antilles” is present

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
    const data = JSON.parse(body).results;
    let count = 0;
    for (const movie in data) {
      const TotalChar = data[movie].characters;
      for (const character in TotalChar) {
        if (TotalChar[character].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
