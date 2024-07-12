#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const options = {
  url: 'https://swapi-api.alx-tools.com/api/films/' + movieID,
  method: 'GET'
};

async function main () {
  try {
    request(options, async function (error, response, body) {
      if (error) throw error;
      const charactersURL = JSON.parse(body).characters;
      for (const link of charactersURL) {
        try {
          const character = await requestPromise(link);
          console.log(character.name);
        } catch (error) {
          console.error(error);
        }
      }
    });
  } catch (error) {
    console.error(error);
  }
}

function requestPromise (url) {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (error, response, body) => {
      if (error) return reject(error);
      resolve(body);
    });
  });
}

main();
