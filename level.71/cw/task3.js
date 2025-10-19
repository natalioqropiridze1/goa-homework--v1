// რიცხვების საწყისი მასივი
let numbers = [10, 20, 30, 40, 50];
console.log("საწყისი მასივი:", numbers);

// pop() შლის ბოლო ელემენტს
let last = numbers.pop();
console.log("pop წაშალა:", last);
console.log(numbers);

// shift() შლის პირველ ელემენტს
let first = numbers.shift();
console.log("shift წაშალა:", first);
console.log(numbers);

// unshift() ამატებს ახალ ელემენტს დასაწყისში
numbers.unshift(5);
console.log("unshift დაამატა 5:", numbers);

// slice() ქმნის ახალ მასივს მითითებული მონაკვეთიდან
let sliced = numbers.slice(1, 3);
console.log("slice(1,3):", sliced);
console.log("ორიგინალი:", numbers);

// splice() შლის ან ამატებს ელემენტებს 
numbers.splice(2, 1, 25, 26);
console.log("splice-ის შემდეგ:", numbers);

// indexOf() აბრუნებს პირველი ინდექსს
console.log("indexOf(25):", numbers.indexOf(25));

// lastIndexOf()  აბრუნებს ბოლო ინდექსს
numbers.push(20); 
console.log("lastIndexOf(20):", numbers.lastIndexOf(20));

// includes()  ამოწმებს არსებობს თუ არა ელემენტი
console.log("includes(40):", numbers.includes(40));  
console.log("includes(100):", numbers.includes(100)); 

// find()  აბრუნებს პირველ ელემენტს, რომელიც აკმაყოფილებს პირობას
let found = numbers.find(num => num > 25);
console.log("find(num > 25):", found);

// findIndex()  აბრუნებს ინდექსს იმ ელემენტის, რომელიც აკმაყოფილებს პირობას
let foundIndex = numbers.findIndex(num => num > 25);
console.log("findIndex(num > 25):", foundIndex);



