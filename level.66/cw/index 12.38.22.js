const input1 = document.getElementById("input1");
    const input2 = document.getElementById("input2");
    const button = document.getElementById("checkBtn");

    button.addEventListener("click", function() {
      let value1 = input1.checked;
      let value2 = input2.checked;

      let andResult = value1 && value2;

      result.innerText = "შედეგი: " + andResult;
    });