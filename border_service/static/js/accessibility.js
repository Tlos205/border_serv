document.addEventListener('DOMContentLoaded', function () {
    const toggleBtn = document.getElementById('accessibility-toggle');
    const panel = document.getElementById('accessibility-panel');
    const closeBtn = document.getElementById('accessibility-close');

    // Открытие/закрытие панели
    toggleBtn.addEventListener('click', () => panel.classList.toggle('active'));
    closeBtn.addEventListener('click', () => panel.classList.remove('active'));

    // Закрытие по клику вне панели
    document.addEventListener('click', (e) => {
        if (!toggleBtn.contains(e.target) && !panel.contains(e.target)) {
            panel.classList.remove('active');
        }
    });

    // Высокий контраст
    document.getElementById('high-contrast').addEventListener('click', () => {
        document.body.classList.toggle('high-contrast');
        localStorage.setItem('highContrast', document.body.classList.contains('high-contrast'));
    });

    // Управление размером шрифта
    const sizes = ['normal', 'large', 'larger', 'largest'];
    const setFontSize = (size) => {
        document.body.classList.remove('font-large', 'font-larger', 'font-largest');
        if (size !== 'normal') document.body.classList.add('font-' + size);
        localStorage.setItem('fontSize', size);
    };

    document.getElementById('font-increase').addEventListener('click', () => {
        let current = localStorage.getItem('fontSize') || 'normal';
        let idx = sizes.indexOf(current);
        if (idx < sizes.length - 1) setFontSize(sizes[idx + 1]);
    });

    document.getElementById('font-decrease').addEventListener('click', () => {
        let current = localStorage.getItem('fontSize') || 'normal';
        let idx = sizes.indexOf(current);
        if (idx > 0) setFontSize(sizes[idx - 1]);
    });

    document.getElementById('font-reset').addEventListener('click', () => setFontSize('normal'));

    // Восстановление сохранённых настроек
    if (localStorage.getItem('highContrast') === 'true') {
        document.body.classList.add('high-contrast');
    }
    const savedSize = localStorage.getItem('fontSize');
    if (savedSize && savedSize !== 'normal') {
        document.body.classList.add('font-' + savedSize);
    }
});