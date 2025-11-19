function outer() {
    let outerr = "natali";
  
    function inner() {
      outerr = outerr +"bruh"
      console.log(outerr); 
    }
  
    inner();
  }
  
  outer();
  
  // Lexical scope means that the accessibility of variables is determined by where they are declared in the code
  // Hoisting means that before JavaScript runs your code it remembers all your variable and function names and 
  // puts them at the top of the file