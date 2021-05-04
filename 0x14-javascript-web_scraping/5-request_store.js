#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const urlId = process.argv[2];
const fileName = process.argv[3];
request(urlId, function (response, body) {
    fs.writeFile(fileName, body.body, 'utf-8', err => {
	if (err) {
	    console.log(err);
	}
    });
});
