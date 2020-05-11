#!/usr/bin/node
// function that returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const element in list) {
    if (list[element] === searchElement) {
      count++;
    }
  }
  return count;
};
