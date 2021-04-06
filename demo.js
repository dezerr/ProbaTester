/**
 * Le nombre généré est entre [0 à #max]
 * La réponse ne bouge pas #answer est une constante
 */

const max = 50;
const answer = 9;
let random = null;
let i = 0;

let red = "\x1b[31m";
let magenta = "\x1b[35m";
let green = "\x1B[32m";
let white = "\x1B[37m";

console.log(red, 'Nombre de tentative : Chiffre random :  Chiffre random à trouver');

setTimeout(() => {
    while (answer !== random) {
        random = Math.round(Math.random() * max);
        console.log(`${magenta} ${i+1} : ${random} : ${answer} `);
        i++;
        if (i === 1 && random === answer) {
            console.log(red, "C'est un perfect");
        } else if (answer === random) {
            console.log(green, `Trouvé à la ${i}ème tentative !`, white);
        
        }
    }
}, 2000)