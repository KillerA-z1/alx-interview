#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2] + '/';
const starWarsApiBaseUrl = 'https://swapi-api.alx-tools.com/api/films/';

// Makes an API request to get film information
request(starWarsApiBaseUrl + movieId, async function (error, response, filmData) {
  if (error) return console.error(error);

  // Parse the response body to get the list of character URLs
  const characterUrlList = JSON.parse(filmData).characters;

  // Iterate through the character URLs and fetch character information
  for (const characterUrl of characterUrlList) {
    await new Promise(function (resolve, reject) {
      request(characterUrl, function (error, response, characterData) {
        if (error) return console.error(error);

        // Parse the character information and print the character's name
        console.log(JSON.parse(characterData).name);
        resolve();
      });
    });
  }
});
