#!/usr/bin/node
// function that converts a number from base 10 to another base
exports.converter = function (base) {
  function InternConv (number) {
    return number.toString(base);
  }
  return InternConv;
};
