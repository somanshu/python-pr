function flatten(arr = []) {
	return arr.reduce(function (acc, curVal) {
		if (!Array.isArray(curVal)) {
			acc.push(curVal);
		} else {
			var a = flatten(curVal);
			acc.concat(a);
		}
		return acc;
	}, []);
}

arr = [{
		val: 10
	},
	[
		1,
		[
			2,
			[
				3,
				[
					4
				]
			]
		]
	]
]
console.log(flatten(arr));
