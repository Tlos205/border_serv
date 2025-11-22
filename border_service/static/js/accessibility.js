function toggleAccessibilityPanel() {
    const panel = document.getElementById('accessibility-panel');
    panel.classList.toggle('hidden');
}

function toggleHighContrast() {
    document.body.classList.toggle('high-contrast');
    localStorage.setItem('highContrast', document.body.classList.contains('high-contrast'));
}

function setFontSize(size) {
    document.body.className = document.body.className.replace(/font-\w+/g, '');
    if (size !== 'normal') {
        document.body.classList.add('font-' + size);
    }
    localStorage.setItem('fontSize', size);
}

function increaseFont() {
    const sizes = ['normal', 'large', 'larger', 'largest'];
    let current = localStorage.getItem('fontSize') || 'normal';
    let next = sizes[Math.min(sizes.indexOf(current) + 1, sizes.length - 1)];
    setFontSize(next);
}

function decreaseFont() {
    const sizes = ['normal', 'large', 'larger', 'largest'];
    let current = localStorage.getItem('fontSize') || 'normal';
    let next = sizes[Math.max(sizes.indexOf(current) - 1, 0)];
    setFontSize(next);
}

function resetFont() {
    setFontSize('normal');
}

// При загрузке страницы — восстановить настройки
document.addEventListener('DOMContentLoaded', () => {
    if (localStorage.getItem('highContrast') === 'true') {
        document.body.classList.add('high-contrast');
    }
    const savedSize = localStorage.getItem('fontSize');
    if (savedSize && savedSize !== 'normal') {
        document.body.classList.add('font-' + savedSize);
    }
});