const products = [
    { id: 1, name: "ლეპტოპი", price: 2500 },
    { id: 2, name: "მობილური", price: 1800 },
    { id: 3, name: "ყურსასმენი", price: 350 },
    { id: 4, name: "სმარტ საათი", price: 900 }
  ];

  const productList = document.getElementById('product-list');
  const cartDiv = document.getElementById('cart');
  let cart = [];


  products.forEach(prod => {
    const div = document.createElement('div');
    div.className = 'product';
    div.innerHTML = `
      <h3>${prod.name}</h3>
      <p>ფასი: ${prod.price}₾</p>
      <button onclick="addToCart(${prod.id})">დამატება</button>
    `;
    productList.appendChild(div);
  });


  function addToCart(id) {
    const item = products.find(p => p.id === id);
    cart.push(item);
    renderCart();
  }
