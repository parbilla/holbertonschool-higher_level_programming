#!/usr/bin/node
const request = require('request');
const urlId = process.argv[2];
request(urlId, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const tasks = JSON.parse(body);
    const dict = {};
    for (const i in tasks) {
      const id = tasks[i].userId;
      if (tasks[i].completed === true) {
        if (dict[id]) {
          dict[id]++;
        } else {
          dict[id] = 1;
        }
      }
    }
    console.log(dict);
  }
});
