document.getElementById('yearBtn').addEventListener('click', checkBirthYear);

function checkBirthYear() {
    const yearInput = document.getElementById('yearInput');
    const birthYear = parseInt(yearInput.value, 10);
    const currentYear = new Date().getFullYear();
    const age = currentYear - birthYear;
    const msg = document.getElementById('ageMsg');
    if (isNaN(age) || birthYear > currentYear || birthYear < 1900) {
        msg.textContent = "Please enter a valid year.";
    } else if (age < 18) {
        msg.textContent = "Minor";
    } else {
        msg.textContent = "Adult";
    }
}