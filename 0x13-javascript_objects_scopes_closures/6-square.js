#!/usr/bin/node
/*
 * a class Square that defines a square and inherits from Rectangle of 4-rectangle.js
 * The constructor must take 1 argument: size
 * constructor of Rectangle must be called (by using super())
 * n instance method called charPrint(c) that prints the rectangle using the character c
 * If c is undefined, use the character X
 */
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) c = 'X';
    let count = 1;
    while (count <= this.height) {
      for (let x = 1; x <= this.width; x++) {
        process.stdout.write(c);
      }
      count++;
      console.log();
    }
  }
}

module.exports = Square;
