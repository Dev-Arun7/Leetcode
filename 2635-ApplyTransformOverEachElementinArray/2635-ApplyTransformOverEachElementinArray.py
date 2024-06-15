/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function (arr, fn) {
    const res = Array(arr.length);
    for (const i in arr) {
        res[i] = fn(arr[i], Number(i))
    }
    return res
};
f
