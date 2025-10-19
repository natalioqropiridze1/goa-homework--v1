let form = document.forms[0];
form.onsubmit = function (event) {
    event.preventDefault();
    let name = document.getElementById('name').value;
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;

    if (name === '' || email === '' || password === '') { 
    alert('Please enter complete information.');
    } else {
    alert('Form submitted successfully!');
    }
}