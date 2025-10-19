
let exam = prompt("insert exam score");
let activity = prompt("insert activity score");


exam = Number(exam);
activity = Number(activity);


let total = exam + activity;

let grade;
if (total >= 90) {
  grade = "(A)";
} else if (total >= 75) {
  grade = "(B)";
} else if (total >= 60) {
  grade = " (C)";
} else if (total >= 50) {
  grade = "(D)";
} else {
  grade = "(Fail)";
}

alert("whole point " + total + " → " + grade);