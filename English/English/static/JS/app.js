const btn = document.getElementById('theme').value;
const theme = document.body.className;
const currentTheme = localStorage.getItem('theme');
console.log(btn, 1);
console.log(theme, 2);
console.log(currentTheme, 3);







/* const btn = document.querySelector('.theme__button')
const theme = document.querySelector('.theme')
const currentTheme = localStorage.getItem('theme')

function setTheme(name) {
    theme.setAttribute('data-theme', name)
    localStorage.setItem('theme', name)
}

if (currentTheme) {
    theme.setAttribute('data-theme', currentTheme)
} else {
    setTheme('light')
}

btn.addEventListener('click', () => {
    if (theme.getAttribute('data-theme') === 'light') {
        setTheme('dark')
    } else if (theme.getAttribute('data-theme') === 'dark') {
        setTheme('soft')
    } else {
        setTheme('light')
    }
}) */ 