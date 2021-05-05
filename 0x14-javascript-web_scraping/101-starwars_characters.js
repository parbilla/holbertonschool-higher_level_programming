#!/usr/bin/node
const request = require('request');
const urlId = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
let charList = [];
request(urlId, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    charList = JSON.parse(body).characters;
    printChar(charList, 0);
  }
});

function printChar (charList, i) {
  request(charList[i], function (err, response, body) {
    if (err) {
      console.log(err);
    } else {
      console.log(JSON.parse(body).name);
      if (i + 1 < charList.length) {
        printChar(charList, i + 1);
      }
    }
  });
}
