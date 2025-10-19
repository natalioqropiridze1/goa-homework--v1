let form = document.forms[0];
form.onsubmit = function (event) {
    event.preventDefault();
    let name = document.getElementById('name').value;
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;
    let confirmPassword = document.getElementById('confirm_password').value;
    if (name === '' || email === '' || password === '' || confirmPassword === '') {
        alert('Please enter complete information.');
    } else if (password.length < 8) {
        alert('Please enter a longer password.');
    } else if (password !== confirmPassword) {
        alert('Passwords do not match.');
    } else if (!email.includes('@') || !email.includes('.')) {
        alert('Please enter a valid email address.');
    } else {
        alert('Registration successful!');
        document.body.innerHTML += `<h2>Welcome, ${name}!</h2>`;
    }}