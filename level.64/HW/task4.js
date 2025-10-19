document.getElementById('lengthBtn').onclick = checkLength;

function checkLength() {
    let word = document.getElementById('wordInput').value;
    let length = word.length;
    document.getElementById('wordOut').innerText = `The word "${word}" has ${length} characters.`;
}