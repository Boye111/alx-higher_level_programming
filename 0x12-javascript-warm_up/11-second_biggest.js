#!/usr/bin/node
const len = process.argv.length;
const nums = process.argv.slice(2).map(function (n) {
  return parseInt(n);
});
const max = Math.max.apply(Math, nums);
const min = Math.min.apply(Math, nums);

if (len > 3) {
  let i = 0;
  let n = 0;
  let secbig = min;

  for (; i < len; ++i) {
    n = nums[i];

    if (n > secbig && n < max) {
      secbig = n;
    }
  }
  console.log(secbig);
} else {
  console.log(0);
}
