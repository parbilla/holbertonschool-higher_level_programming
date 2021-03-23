#!/usr/bin/node
// Define the class of a rectangle
module.exports = class Rectangle {
    constructor(w, h) {
        if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
        }
    }
    print() {
        for (let i = 0; i < this.height; i++) {
            let sq = '';
            for (let j = 0; j < this.width; j++) {
              sq = sq + 'X';
            }
            console.log(sq);
        }
    }
};
