#!/usr/bin/node
const request = require('request');
const reqChar = require('request');
const urlId = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
let charList = [];
request(urlId, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    charList = JSON.parse(body).characters;
    for (const i in charList) {
      reqChar(charList[i], function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
