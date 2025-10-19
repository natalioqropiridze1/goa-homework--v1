document.getElementById('reverseBtn').onclick = reverseWord;

function reverseWord() {
let word = document.getElementById('wordInput').value;
let reversed = word.split('').reverse().join('');
document.getElementById('wordOut').textContent = reversed;
}