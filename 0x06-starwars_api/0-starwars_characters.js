#!/usr/bin/node

const request = require('request');

// Function to fetch and print character names in exact order
const exactOrder = (actors, index) => {
  if (index === actors.length) return;
  request(actors[index], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    exactOrder(actors, index + 1);
  });
};

// Main function to fetch the movie data
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const actors = JSON.parse(body).characters;
  exactOrder(actors, 0);
});
