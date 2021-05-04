#!/usr/bin/node
const request = require('request');
const urlId = process.argv[2] + '/?format=json';
let cont = 0;
const name = 'https://swapi-api.hbtn.io/api/people/18/';
request.get(urlId, function (response, body) {
  const filmList = (JSON.parse(body.body).results);
  for (let film in filmList) {
    for (let i in filmList[film].characters) {
      if (filmList[film].characters[i] === name) {
        cont++;
      }
    }
  }
  console.log(cont);
});
