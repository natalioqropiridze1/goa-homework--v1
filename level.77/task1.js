const userForm = document.getElementById('userForm');
const usersTable = document.querySelector('#userTable tbody');

// Container — ამზადებს <tr> ელემენტს და ავსებს მონაცემებით
function buildRow(nameValue, mailValue, phoneValue) {
  const tableRow = document.createElement('tr');

  const tdName = document.createElement('td');
  const tdMail = document.createElement('td');
  const tdPhone = document.createElement('td');

  tdName.textContent = nameValue;
  tdMail.textContent = mailValue;
  tdPhone.textContent = phoneValue;

  tableRow.appendChild(tdName);
  tableRow.appendChild(tdMail);
  tableRow.appendChild(tdPhone);

  return tableRow;
}

// Presentational — ამატებს მზად <tr> ცხრილში
function renderRow(rowNode) {
  usersTable.appendChild(rowNode);
}

// ფორმის გაგზავნა
userForm.addEventListener('submit', function (e) {
  e.preventDefault();

  const enteredName = document.getElementById('fullName').value;
  const enteredEmail = document.getElementById('email').value;
  const enteredPhone = document.getElementById('phone').value;

  const createdRow = buildRow(enteredName, enteredEmail, enteredPhone);
  renderRow(createdRow);

  userForm.reset();
});
