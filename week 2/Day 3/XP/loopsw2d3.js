// var names = ["john", "sarah", 12, "Rudolf",34]

// for (var name of names) {
//     if(typeof name === string && name != name.charAt(0).toUpperCase() {
//                var newname = name.charAt(0).toUpperCase();
//                console.log(newname);
//     }

// }


var names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]

var newname = names.sort();
var cn = '';

for(var x of newname) {
    var firstletter = x.charAt(0);
    cn = cn.concat(firstletter);
}
console.log(cn);


