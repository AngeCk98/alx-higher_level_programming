#!/usr/bin/node

/*
 * A script that prints a factorial
 */

const arg1 = process.argv[2];

/* function fact (num) {
  if (isNaN(num) === true) {
    num = 1;
    return (num);
  } else if (isNaN(num) === false) {
    for (let i = 1; i <= num; i++) {
      num = num * i;
    }
    return (num);
  }
}
console.log(fact(varFact));
*/

function calcFact (num) {
  if ((isNaN(num) === true) || (num === 1)) {
    num = 1;
    return (num);
  } else {
    return num * calcFact(num - 1);
  }
}
console.log(calcFact(arg1));
