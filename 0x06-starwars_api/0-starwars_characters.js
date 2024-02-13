#!/usr/bin/node

const request = require('request');

const getCharacters = (arr, idx) => {
  if (idx === arr.length) return;
  request(arr[idx], (err, response, body) => {
    if (err) {
      throw err;
    } else {
      console.log(JSON.parse(body).name);
      getCharacters(arr, idx + 1);
    }
  });
};

request(
  `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  (err, response, body) => {
    if (err) {
      throw err;
    } else {
      const chars = JSON.parse(body).characters;
      getCharacters(chars, 0);
    }
  }
);
