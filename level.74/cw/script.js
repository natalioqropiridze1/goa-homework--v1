    const allDivs = document.getElementsByTagName('div');
    console.log('div elements', allDivs);


    const products = document.getElementsByClassName('product');
    console.log('product class elements', products);


    const secondProduct = products[1];
    console.log('prevous elements', secondProduct.previousElementSibling);


    console.log('nect elemet', secondProduct.nextElementSibling);


    const special = document.getElementById('special-product');
    console.log('first child element', special.firstChild);


    console.log('last child ', special.lastChild);
