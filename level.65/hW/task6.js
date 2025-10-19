const tablet = {
    brand: 'Apple',
    model: 'iPad Pro',
    color: 'Silver',
    playMusic: function() {
        console.log('Playing music...');
    }
};
document.getElementById('musicBtn').onclick = tablet.playMusic.bind(tablet);  