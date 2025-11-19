const parent = document.getElementById('parent');
const child = document.getElementById('child');


parent.addEventListener('click', () => {
  console.log('Parent clicked');
});

child.addEventListener('click', () => {
  console.log('Child clicked');
});


parent.addEventListener('click', () => {
  console.log('Parent clicked - capturing');
}, true);

child.addEventListener('click', () => {
  console.log('Child clicked');
});

