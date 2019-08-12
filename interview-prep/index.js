Array.isArray = function (obj) {
	return Object.prototype.toString.call(obj) === '[object Array]';
}

var is_array = function (value) {
	return value &&
		typeof value === 'object' &&
		typeof value.length === 'number' &&
		typeof value.splice === 'function' &&
		!(value.propertyIsEnumerable('length'));
};

// Debounce polyfill
function debounce(fn, time) {
	var timerId;
	return function () {
		args = Array.prototype.slice(arguments);
		clearTimeout(timerId);
		timerId = setTimeout(() => fn.apply(this, args), time);
	}
}
