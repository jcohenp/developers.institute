var food = "The food was not bad.";
var x = food.indexOf("not");
var y = food.indexOf("bad");
if (y>x) {
    console.log("The food was good.");
}
else {
    console.log(food);
}