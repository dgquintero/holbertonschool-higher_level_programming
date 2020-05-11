#!/usr/bin/node
// class Rectangle that defines a rectangle
module.exports = class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  // instance Method
  print() {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
  // instance Method
  rotate() {
    let tmp = this.height;
    this.height = this.width;
    this.width = tmp;
  }
  // instance Method
  double() {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
