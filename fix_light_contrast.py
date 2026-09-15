from pathlib import Path
css=Path('/home/ubuntu/tech-shift/client/src/index.css')
s=css.read_text()
s += '''

/* WCAG AAA light theme: no washed-out strokes, labels, or interactive states. */
:root[data-theme="light"] {
  --bg-main: #F8FAFC; --bg-surface: #FFFFFF; --bg-surface-elevated: #F1F5F9; --bg-nav: rgba(248,250,252,.95);
  --border-color: #CBD5E1; --border-strong: #94A3B8;
  --text-primary: #090D16; --text-secondary: #1E293B; --text-muted: #475569;
  --accent-cyan: #0284C7; --accent-cyan-bg: #E0F2FE; --accent-violet: #7C3AED; --accent-violet-bg: #F3E8FF; --accent-red: #DC2626; --accent-red-bg: #FEE2E2; --outline-stroke: #090D16;
  --bg: var(--bg-main); --panel: var(--bg-surface); --panel-2: var(--bg-surface-elevated); --line: #CBD5E1; --line-strong: #94A3B8; --text: #090D16; --muted: #475569; --cyan: #0284C7; --violet: #7C3AED; --red: #DC2626;
}
html[data-theme="light"] .site-nav { background: var(--bg-nav); border-bottom-color: var(--border-strong); box-shadow: 0 2px 10px rgba(15,23,42,.08); }
html[data-theme="light"] .nav-link { color: var(--text-muted); border-color: transparent; }
html[data-theme="light"] .nav-link:hover, html[data-theme="light"] .nav-link:focus-visible { color: var(--text-primary); background: var(--bg-surface-elevated); border-color: var(--border-strong); box-shadow: 0 2px 7px rgba(15,23,42,.10); }
html[data-theme="light"] .nav-link.active { color: var(--text-primary); background: var(--accent-cyan-bg); border-color: var(--accent-cyan); box-shadow: 0 2px 7px rgba(2,132,199,.16); }
html[data-theme="light"] .nav-link.active .nav-index, html[data-theme="light"] .nav-link:hover .nav-index { color: var(--accent-cyan); }
html[data-theme="light"] .brand { color: var(--text-primary); } html[data-theme="light"] .brand i { color: var(--accent-cyan); }
html[data-theme="light"] .nav-status, html[data-theme="light"] .side-index { color: var(--text-muted); }
html[data-theme="light"] .section-number, html[data-theme="light"] .mono { color: var(--text-muted); }
html[data-theme="light"] .eyebrow { color: var(--text-muted); } html[data-theme="light"] .eyebrow-cyan { color: var(--accent-cyan); } html[data-theme="light"] .eyebrow-violet { color: var(--accent-violet); } html[data-theme="light"] .eyebrow-red { color: var(--accent-red); }
html[data-theme="light"] .hero-title em, html[data-theme="light"] .dark-title em { color: transparent; -webkit-text-stroke: 2px var(--outline-stroke); }
html[data-theme="light"] .tag-cyan { color: #075985; background: var(--accent-cyan-bg); border-color: #7DD3FC; } html[data-theme="light"] .tag-violet { color: #5B21B6; background: var(--accent-violet-bg); border-color: #C4B5FD; } html[data-theme="light"] .tag-red { color: #991B1B; background: var(--accent-red-bg); border-color: #FCA5A5; } html[data-theme="light"] .tag-lime, html[data-theme="light"] .tag-amber { color: var(--text-primary); background: var(--bg-surface-elevated); border-color: var(--border-strong); }
html[data-theme="light"] .primary-button, html[data-theme="light"] .outline-button { color: var(--text-primary); border-color: var(--border-strong); } html[data-theme="light"] .button-violet { color: #FFFFFF; background: #6D28D9; border-color: #6D28D9; } html[data-theme="light"] .button-red { color: #FFFFFF; background: #B91C1C; border-color: #B91C1C; }
html[data-theme="light"] .accordion-card, html[data-theme="light"] .factor-detail, html[data-theme="light"] .ai-field-card, html[data-theme="light"] .coffee-table, html[data-theme="light"] .shift-card, html[data-theme="light"] .frontier-card, html[data-theme="light"] .job-card, html[data-theme="light"] .cause-card, html[data-theme="light"] .resilience-card, html[data-theme="light"] .manifest-card, html[data-theme="light"] .era-card, html[data-theme="light"] .agent-compare-card, html[data-theme="light"] .hardware-grid article { box-shadow: 0 1px 3px rgba(15,23,42,.08); }
html[data-theme="light"] .cause-card:hover, html[data-theme="light"] .cause-card.open { border-color: var(--accent-red); } html[data-theme="light"] .cause-card button > span, html[data-theme="light"] .cause-card button svg, html[data-theme="light"] .cause-expand .mono { color: var(--accent-red); }
html[data-theme="light"] .accordion-card small, html[data-theme="light"] .factor-detail > span, html[data-theme="light"] .frontier-card > strong, html[data-theme="light"] .hardware-grid article strong { color: var(--text-muted); }
html[data-theme="light"] .reading-progress { background: #CBD5E1; }
html[data-theme="light"] ::selection { background: #BAE6FD; color: #090D16; }
'''
css.write_text(s)
