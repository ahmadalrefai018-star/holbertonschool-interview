#!/usr/bin/node
const request = require('request');

function getJson (url) {
  return new Promise((resolve, reject) => {
    request({ url, json: true }, (error, response, body) => {
      if (error) {
        return reject(error);
      }

      if (response.statusCode !== 200) {
        return reject(new Error(`HTTP ${response.statusCode} for ${url}`));
      }

      resolve(body);
    });
  });
}

async function printCharacters (movieId) {
  const film = await getJson(`https://swapi-api.hbtn.io/api/films/${movieId}/`);

  for (const url of film.characters) {
    const character = await getJson(url);
    console.log(character.name);
  }
}

printCharacters(process.argv[2]).catch(error => {
  console.error(error.message);
  process.exitCode = 1;
});
