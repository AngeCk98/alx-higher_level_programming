#!/usr/bin/node

/*
 * script that prints a message depending
 *on the number of arguments passed:
 */

const myVar = process.argv.length - 2;

if (myVar === 0) {
  console.log('No argument');
} else if (myVar === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
