const limit = parseInt(process.argv[0]);

if (limit) {
	for (let i = 0; i < limit; ++i) {
		console.log("C is fun");
	}
} else {
	console.log("Missing number of occurrences");
}
