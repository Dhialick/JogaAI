const menu = document.getElementById('side_menu');
const toggle = document.getElementById('menu_botao');
const overlay = document.getElementById('overlay');

toggle.addEventListener('click', () => {
  menu.style.left = '0';
  overlay.style.display = 'block';
});

overlay.addEventListener('click', () => {
  menu.style.left = '-250px';
  overlay.style.display = 'none';
});
