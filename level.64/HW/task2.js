document.getElementById('doubleBtn').onclick = doubleNumber;

function doubleNumber() {
    let num = document.getElementById('numInput').value;
    let doubled = num * 2;
    document.getElementById('numOut').innerText = doubled;
}