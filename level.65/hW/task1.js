const laptop = {
    brand: 'Dell', 
    ram: '32gb',  
    price: 500,   
    turnOn: function() { 
        console.log("Laptop is on");
    }
};

document.getElementById('laptopBtn').addEventListener('click', function() {
    laptop.turnOn();
});

function turnOn(){
    console.log("Laptop is on")
}