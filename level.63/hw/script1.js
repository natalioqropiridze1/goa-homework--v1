document.getElementById("nameBtn").addEventListener("click", showName);

function showName() {
    const name = prompt("Enter your name");
    document.getElementById("output").innerText = name;
}   