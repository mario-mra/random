// Dirty

var msg = document.getElementsByClassName("message")[0]["innerText"];
msg = msg.substr(26,1024);
fetch('https://raw.githubusercontent.com/emn178/js-sha512/master/src/sha512.js').then(response => response.text()).then(text => eval(text))
var result = sha512(msg);
window.open('https://ringzer0ctf.com/challenges/13/'+result)
