#!/usr/bin/node
// function that returns the reversed version of a list

exports.esrever = function (list) {
  const NewList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    NewList.push(list[i]);
  }
  return NewList;
};
