var array = ["Banana", "Apples", "Orangers", "blueberries"]
array.shift();
console.log(array);
array.push("Kiwi");
console.log(array)
array.splice(-0,1)
console.log(array)
// var newArray
// newArray = array.sort();
// console.log(newArray); Doesn't work



var array2 = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(array2[1][1][0]);