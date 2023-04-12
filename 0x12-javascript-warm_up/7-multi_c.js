#!/usr/bin/node

/*
 * A script that prints x times “C is fun”
 */

const myVar = process.argv[2];
if (myVar === undefined) {
  console.log('Missing number of occurences');
}
for (let i = 0; i < myVar; i++) {
  console.log('C is fun');
}
