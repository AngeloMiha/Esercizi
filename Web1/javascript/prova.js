const prompt = require('prompt-sync')();

var sPrimoNum = prompt("Inserisci il primo numero: ");
var iPrimoNum = parseInt(sPrimoNum)

var sSecondoNum = prompt("Inserisci il secondo numero: ");
var iSecondoNum = parseInt(sSecondoNum)

var sSomma = iPrimoNum + iSecondoNum
console.log("La somma è: "+ sSomma);

