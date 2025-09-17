const colors={HTML:"#e34f26",CSS:"#1572B6",JS:"#f7df1e"};
const svg=lang=>`data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='256' height='256'><rect width='100%' height='100%' fill='${colors[lang]}'/><text x='50%' y='50%' dominant-baseline='middle' text-anchor='middle' font-family='Arial, Helvetica, sans-serif' font-weight='700' font-size='96' fill='${lang==="JS"?'#000':'#fff'}'>${lang}</text></svg>`;
document.querySelectorAll('button').forEach(btn=>{
btn.onclick=()=>{
document.getElementById('logo').src=svg(btn.dataset.lang);
};
});