function add(a, b) {
	return a + b;
}

const a = parseInt(process.argv[0]);
const b = parseInt(process.argv[1]);

console.log(add(a, b));
