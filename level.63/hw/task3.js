document.getElementById("passBtn").addEventListener("click", getPassword);
function getPassword() {
    const password = prompt("Enter your password");
    document.getElementById("passOut").innerText = password;
}