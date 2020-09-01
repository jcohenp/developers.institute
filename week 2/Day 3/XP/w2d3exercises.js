// const GUEST_LIST = {
//     Randy: "Germany",
//     Karla: "France",
//     Wendy: "Japan",
//     Norman: "England",
//     Sam: "Argentina"
//   }
//   var name = prompt("What is your name?");
//   for (var x in GUEST_LIST) {
//       if (x = name){
//         console.log("Hi! I'm " + x + " from " + GUEST_LIST.x)
//         alert ("Hi! I'm " + x + " from " + GUEST_LIST.x)
//       }

//       else {
//           console.log("Hi! I am a guest.")
//           alert("Hi! I am a guest.")
//       }

//     }

// var name = prompt("What is your name?");
// let newname = name.charAt(0).toUpperCase() + name.slice(1)
// if (GUEST_LIST[newname]){
//             console.log("Hi! I'm " + newname + " from " + GUEST_LIST[newname])
//             alert ("Hi! I'm " + newname + " from " + GUEST_LIST[newname])
//           }
// else {
//     console.log("Hi! I am a guest.")
//     alert("Hi! I am a guest.")
// }




var colours = ["purple", "blue", "gold"];

for (var x of colours) {

    if (x == colours[1]) {
        console.log("My favourite colour is " + x);

    }

    if (x == colours[0]) {
    
        console.log("My second favourite colour is " + x);
    }

    if (x == colours[2]) {
        console.log("My third favourite colour is " + x)
    }
}    

// why does code run more than once?    

