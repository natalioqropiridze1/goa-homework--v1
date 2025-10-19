document.getElementById("ageBtn").addEventListener("click", showAge);
function showAge() {
    const age = document.getElementById("ageInput").value;
    document.getElementById("ageOut").innerText = age;
}