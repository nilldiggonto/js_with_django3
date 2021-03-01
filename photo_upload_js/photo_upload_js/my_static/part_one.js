console.log('hlw something')

let a = document.getElementById('p1').innerText;
console.log(a)
//Getting List from a unnecessary text
var first = a.indexOf(':')
var last = a.indexOf('.',first+1)
var list_output = a.substring(first+1,last)
// document.getElementById('o1').innerHTML = list_output;
//split
console.log(list_output)
document.getElementById('o1').innerHTML = list_output.split(',')




// will work later.. 