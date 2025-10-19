let dataBase = [];

    function register() {
      let name = document.getElementById("name").value;
      let email = document.getElementById("email").value;
      let password = document.getElementById("password").value;


   let account = {
    name: name,
    email: email,
    password: password
  };

  dataBase.push(account);

  console.log(dataBase);

  document.getElementById("name").value = "";
  document.getElementById("email").value = "";
  document.getElementById("password").value = "";
}