const input = document.getElementById("taskInput");
const addBtn = document.getElementById("addBtn");
const list = document.getElementById("taskList");

addBtn.addEventListener("click", function() {
  const task = input.value.trim(); 

  if (task !== "") { 
    const li = document.createElement("li");
    li.textContent = task;
    list.appendChild(li);
    input.value = ""; 
  } else {
    alert("please insertt");
  }
});