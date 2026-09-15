from pathlib import Path
p=Path('/home/ubuntu/tech-shift/client/src/index.css')
s=p.read_text()
s += '''

/* User-controlled readability preferences */
:root[data-text-scale="large"] { font-size: 112.5%; }
:root[data-text-scale="xlarge"] { font-size: 125%; }
.accessibility-toggle { min-width: 29px; padding: 7px 8px; border: 1px solid var(--border-color); background: var(--bg-surface); color: var(--text-secondary); font: 10px var(--mono); transition: color .18s var(--ease-out), background .18s var(--ease-out), border-color .18s var(--ease-out), transform .18s var(--ease-out); }
.accessibility-toggle:hover, .accessibility-toggle:focus-visible { border-color: var(--accent-cyan); background: var(--bg-surface-hover); color: var(--accent-cyan); transform: translateY(-1px); outline: none; }
.accessibility-toggle.is-active { border-color: var(--accent-violet); background: var(--accent-violet-bg, rgba(124,58,237,.12)); color: var(--accent-violet); }
.accessibility-toggle span { color: var(--accent-cyan); }
.technology-card { position: relative; transition: transform .22s var(--ease-out), box-shadow .22s var(--ease-out), border-color .22s var(--ease-out), background .22s var(--ease-out); }
.technology-card:hover, .technology-card:focus-within { transform: translateY(-5px); box-shadow: 0 14px 30px rgba(15,23,42,.14); border-color: var(--accent-cyan); }
.technology-card::after { content: attr(data-tooltip); position: absolute; z-index: 20; left: 18px; right: 18px; bottom: calc(100% + 10px); padding: 10px 12px; border: 1px solid var(--accent-cyan); background: var(--bg-surface); color: var(--text-primary); font: 11px/1.5 var(--mono); opacity: 0; pointer-events: none; transform: translateY(5px); transition: opacity .18s var(--ease-out), transform .18s var(--ease-out); box-shadow: 0 10px 24px rgba(15,23,42,.16); }
.technology-card:hover::after, .technology-card:focus-within::after { opacity: 1; transform: none; }
html[data-contrast="high"] { --bg-main: #FFFFFF; --bg-surface: #FFFFFF; --bg-surface-hover: #E2E8F0; --border-color: #334155; --text-primary: #000000; --text-secondary: #0F172A; --text-muted: #334155; --accent-cyan: #005A8D; --accent-violet: #5B21B6; --accent-red: #B91C1C; --accent-cyan-bg: #E0F2FE; --accent-violet-bg: #F3E8FF; }
html[data-theme="dark"][data-contrast="high"] { --bg-main: #000000; --bg-surface: #0B1220; --bg-surface-hover: #1E293B; --border-color: #CBD5E1; --text-primary: #FFFFFF; --text-secondary: #F1F5F9; --text-muted: #CBD5E1; --accent-cyan: #67E8F9; --accent-violet: #C4B5FD; --accent-red: #FCA5A5; }
html[data-contrast="high"] body, html[data-contrast="high"] .section, html[data-contrast="high"] .hero, html[data-contrast="high"] .dark-section, html[data-contrast="high"] .final-blackout { color: var(--text-primary); }
html[data-contrast="high"] .technology-card, html[data-contrast="high"] .accordion-card, html[data-contrast="high"] .cause-card, html[data-contrast="high"] .factor-detail, html[data-contrast="high"] .factor-list button, html[data-contrast="high"] .future-map-card { border-width: 2px; }
html[data-contrast="high"] .site-nav { border-bottom-color: var(--border-color); }
html[data-contrast="high"] :focus-visible { outline: 3px solid var(--accent-cyan); outline-offset: 3px; }
@media (max-width: 760px) { .nav-status .accessibility-toggle { display: none; } .technology-card::after { left: 8px; right: 8px; bottom: auto; top: calc(100% + 8px); } }
'''
p.write_text(s)
