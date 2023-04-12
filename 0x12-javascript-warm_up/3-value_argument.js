#!/usr/bin/node

/*
 * script that prints the first argument passed to it
 */

const firstVar = process.argv[2];

if (firstVar === undefined) {
  console.log('No argument');
} else {
  console.log(firs
