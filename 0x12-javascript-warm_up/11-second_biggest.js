#!/usr/bin/node

/*
 * A script that searches the second
 *biggest integer in the list of arguments
 */

// let a = process.argv[2];
// let b = process.argv[3];
/* const size = (process.argv.length) - 2;
let i = 0;
for (; i < myArray.length; i++) {
  let tempElem = myArray[i];
  for (let j = i + 1; j < myArray.length, j++) {
    if (tempElem > myArray[j]) {
      tempElem = myArray[j];
  }
}
const index = ;
*/

let nextBigest = 0;
const args = process.argv.slice(2);
if (args.length > 1) {
  args.sort((a, b) => a - b);
  args.pop();
  nextBigest = args[args.length - 1];
}
console.log(nextBigest);
