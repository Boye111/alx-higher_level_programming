#!/usr/bin/node
const arg = parseInt(process.argv[0])

if (arg) {
	console.log('My number: ' + arg);
} else {
	console.log('Not a number');
