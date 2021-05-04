#!/usr/bin/node
const request = require('request');
const urlId = process.argv[2] + '/?format=json';
let cont = 0;
request.get(urlId, function (response, body) {
  const filmList = (JSON.parse(body.body).results);
  for (const film in filmList) {
    for (const i in filmList[film].characters) {
      if (filmList[film].characters[i].includes('18')) {
        cont++;
      }
    }
  }
  console.log(cont);
});
