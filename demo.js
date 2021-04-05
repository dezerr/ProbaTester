const max = 10;
const answer = 8;
let random = null;
let i = 0;

let red = "\x1b[31m";
let magenta = "\x1b[35m";

console.log(red, 'Nombre de tentative : Chiffre random :  Chiffre random à trouver');

setTimeout(() => {
    while (answer !== random) {
        random = Math.round(Math.random() * max);
        console.log(`${magenta} ${i+1} : ${random} : ${answer} `);
        i++;
        if (i === 1 && random === answer) {
            console.log("C'est un perfect");
        }
    }
}, 2000)

