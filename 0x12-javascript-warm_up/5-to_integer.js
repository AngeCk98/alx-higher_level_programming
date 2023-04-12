#!/usr/bin/node

/*
 * A script that prints My number: <first argument
 *converted in integer> if the first argument
 *can be converted to an integer
 */

const varString = process.argv[2];
if ((isNaN(varString)) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + varString);
}
