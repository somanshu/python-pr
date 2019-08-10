function reverse(str) {
	var i = 0;
	var j = str.length - 1;
	var arr = str.split('');

	while (i < j) {
		var tmp = arr[i];
		arr[i] = arr[j];
		arr[j] = tmp;
		i++;
		j--;
	}

	console.log(arr.join(''));
}

reverse('somanshu');
