const arr = [5,0,9,1,7,4,2,6,3,8];
var n = arr.length-1;
var x = arr;

do {
    swapp = false;
    for (var i = 0; i < n; i++) 
      {
        if (x[i]< x[i+1]) {
            var temp = x[i];
             x[i] = x[i+1];
             x[i+1] = temp;
             swapp = true;
            }           
        }        

    n.length--;

    }
while (swapp); { 
    console.log(x)
}

