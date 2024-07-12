#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

async function getCharacterName (characters, index, names = []) {
  if (index === characters.length) {
    names.forEach((name) => console.log(name));
    return;
  }
  const characterPath = characters[index];
  request(characterPath, (error, response, body) => {
    if (error) {
      console.log(error);
    } else if (response.statusCode !== 200) {
      console.error('Unexpected status code:', response.statusCode);
    } else {
      // console.log(JSON.parse(body).name);
      names.push(JSON.parse(body).name);
      getCharacterName(characters, index + 1, names);
    }
  });
}
if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <filmId>');
  process.exit(1);
}
async function getMovies () {
  request(url, (error, response, body) => {
    if (error) {
      console.log(error);
    } else if (response.statusCode !== 200) {
      console.error('Unexpected status code:', response.statusCode);
    } else {
      const characters = JSON.parse(body).characters;
      getCharacterName(characters, 0);
    }
  });
}
getMovies();
