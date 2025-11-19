async function getProducts() {
    const response = await fetch("https://fakestoreapi.com/products");
    const products = await response.json();
  
    const container = document.getElementById("products-container");
    container.innerHTML = "";
  
    products.forEach((product) => {
      const card = document.createElement("div");
      card.classList.add("product-card");
  
      card.innerHTML = `
        <h3>${product.title}</h3>
        <p>Category: ${product.category}</p>
        <img src="${product.image}" width="150">
      `;
  
      container.appendChild(card);
    });
  }
  
  getProducts();