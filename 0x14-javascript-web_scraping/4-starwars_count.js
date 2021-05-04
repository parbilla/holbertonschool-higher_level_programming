#!/usr/bin/node
const request = require('request');
const urlId = process.argv[2];
request(urlId, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const filmList = JSON.parse(body).results;
    let cont = 0;
    for (const film in filmList) {
      for (const i in filmList[film].characters) {
        if (filmList[film].characters[i].includes('18')) {
          cont++;
        }
      }
    }
    console.log(cont);
  }
});
