document.getElementById("showBtn").addEventListener("click", displayText);
function displayText() {
    const inputText = document.getElementById("userInput").value;
    document.getElementById("display").innerText = inputText;
}