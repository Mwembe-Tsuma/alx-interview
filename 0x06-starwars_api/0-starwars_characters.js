#!/usr/bin/node

const request = require('request');

function getCharacters(movieId) {
  const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

  request(apiUrl, { json: true }, (err, res, body) => {
    if (err) {
      console.error('Error fetching data:', err);
      return;
    }

    if (res.statusCode !== 200) {
      console.error(`Unexpected status code: ${res.statusCode}`);
      return;
    }

    const characters = body.characters;

    characters.forEach(characterUrl => {
      request(characterUrl, { json: true }, (err, res, characterBody) => {
        if (err) {
          console.error('Error fetching character data:', err);
          return;
        }

        if (res.statusCode !== 200) {
          console.error(`Unexpected status code: ${res.statusCode}`);
          return;
        }

        console.log(characterBody.name);
      });
    });
  });
}

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as a command line argument.');
} else {
  getCharacters(movieId);
}
