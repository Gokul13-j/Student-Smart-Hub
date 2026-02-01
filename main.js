/**
 * Student Smart Hub - Main JS
 * Theme toggle, nav, AI chat
 */
(function () {
  const themeKey = 'student-smart-hub-theme';
  const saved = localStorage.getItem(themeKey);
  if (saved === 'light') document.documentElement.setAttribute('data-theme', 'light');

  document.addEventListener('click', (e) => {
    const toggle = e.target.closest('.theme-toggle');
    if (toggle) {
      const html = document.documentElement;
      const next = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      html.setAttribute('data-theme', next);
      localStorage.setItem(themeKey, next);
      toggle.textContent = next === 'dark' ? '🌙' : '☀️';
    }
  });

  const themeBtn = document.querySelector('.theme-toggle');
  if (themeBtn && document.documentElement.getAttribute('data-theme') === 'light') themeBtn.textContent = '☀️';
  else if (themeBtn) themeBtn.textContent = '🌙';
})();

// Portal view switcher (student/faculty dashboards)
document.querySelectorAll('[data-view]').forEach(el => {
  el.addEventListener('click', function(e) {
    e.preventDefault();
    var view = this.getAttribute('data-view');
    document.querySelectorAll('.view-panel').forEach(function(p) { p.classList.remove('active'); });
    document.querySelectorAll('[data-view]').forEach(function(l) { l.classList.remove('active'); });
    var panel = document.getElementById('view-' + view);
    if (panel) panel.classList.add('active');
    this.classList.add('active');
  });
});
