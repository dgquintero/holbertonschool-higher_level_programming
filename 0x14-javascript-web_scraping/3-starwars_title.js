#!/usr/bin/node
// Write a script that prints the title of a
// Star Wars movie where the episode number matches a given integer.
const request = require('request');
const MovieID = process.argv[2];
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + MovieID,
  method: 'GET'
};

request(options, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
