var A;
var B;
A = 3;
B = "buongiorno a tutti";
console.log("Il tipo della var A e' " + typeof(A) + "\n");
console.log("Il tipo della var B e' " + typeof (B) + "\n");
var A;
var B;
A = 3;
B = "buongiorno a tutti";
console.log("Il tipo della var A e' " + typeof(A) + "\n");
console.log("Il tipo della var B e' " + typeof (B) + "\n");


function TerminaConLettera(sStringa, STermine) {
    // prendi lunghezza di sTermine
    var lunghezzaTermine = STermine.length;

    // Usa indexOf partendo da sStringa - lunghezza di sTermine
    var posizioneInizio = sStringa.length - lunghezzaTermine;
    var risultato = sStringa.indexOf(STermine, posizioneInizio);

    // ritorna 0 oppure 1
    if (risultato !== -1 && risultato === posizioneInizio) {
        return 1;
    } else {
        return 0;
    }
}

console.log(TerminaConLettera("Ciao mondo", "mondo"));
console.log(TerminaConLettera("Ciao mondo", "Ciao"));
console.log(TerminaConLettera("Ciao mondo", "o"));
console.log(TerminaConLettera("Ciao mondo", "Mondo"));
