#!/usr/bin/node

/*
 * A script that prints a square
 */

const myVar = isNaN(process.argv[2]);
const size = process.argv[2];

if (myVar === true) {
  console.log('Missing size');
} else if (myVar === false) {
  for (let i = 0; i < size; i++) {
    // for (let j = 0; j < size; j++) {
    console.log('X'.repeat(size));
    // }
    // console.log('');
  }
}
