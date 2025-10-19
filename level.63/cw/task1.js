let title = document.getElementById("title");
let input = document.getElementById("username");
let btn = document.getElementById("updateBtn");


btn.onclick = function() {
    title.textContent = "Hello " + input.value;}