let username = 'my name';
let bonusBalance = 1000;

let fireBonus = 0;

let day = 0;

while(day < 7){
    if(day%2 == 0)
        bonusBalance += 50;
    fireBonus += 3;
    day++;
}

bonusBalance -= fireBonus;

console.log(bonusBalance);

alert(`Твой баланс = ${bonusBalance}`);