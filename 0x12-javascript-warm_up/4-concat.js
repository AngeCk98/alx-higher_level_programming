#!/usr/bin/node

/*
 * script that prints two arguments passed
 *to it, in the following format: "is"
 */

const fixedVarString = ((process.argv[2]) + ' is ' + (process.argv[3]));
console.log(fixedVarString);
