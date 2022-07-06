"use strict";

const dados = require("./dados.json");
var somaTotal = 0;
var media = 0;


for (let i = 0; i < dados.length; i++) {
	somaTotal = somaTotal + dados[i].valor;
}


media = somaTotal / dados.length;
console.log("Média: " + media);



for (let i = 0; i < dados.length; i++) {
    if (dados[i].valor > media) {
        console.log("dia: " + dados[i].dia + " valor: " + dados[i].valor);
    }
}