// function to set a given theme/color-scheme
function setTheme(themeName) {
    localStorage.setItem('theme', themeName);
    document.documentElement.className = themeName;
}
// function to toggle between light and dark theme
function toggleTheme() {
    if (localStorage.getItem('theme') === 'theme-pink') {
        setTheme('theme-pink');
    } else {
        setTheme('theme-peach');
    }
}
// Immediately invoked function to set the theme on initial load
(function () {
    if (localStorage.getItem('theme') === 'theme-peach') {
        setTheme('theme-peach');
    } else {
        setTheme('theme-pink');
    }
})();
