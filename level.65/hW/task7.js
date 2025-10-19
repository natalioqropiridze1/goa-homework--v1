document.getElementById('cubeBtn').onclick = cubeNumber;

function cubeNumber() {
    let num = document.getElementById('numInput').value;
    let cube = num ** 3;
    document.getElementById('numOut').textContent = cube;
}