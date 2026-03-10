let count = 0
let target = 250

let counter = setInterval(function(){

count++

document.getElementById("donorCount").innerText = count

if(count >= target){
clearInterval(counter)
}

},20)