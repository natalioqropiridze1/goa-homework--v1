document.getElementById('cityBtn').onclick = getCity;

function getCity() {
    let city = prompt("Enter your city");
    document.getElementById('cityOut').innerText = city;
}