from pathlib import Path
p=Path('/home/ubuntu/tech-shift/client/src/pages/Home.tsx')
s=p.read_text()
s=s.replace('theme: "slate" | "pitch"; toggleTheme: () => void', 'theme: "dark" | "light"; toggleTheme: () => void')
s=s.replace('theme === "slate" ? "Pitch Black" : "Dark Slate"', 'theme === "dark" ? "Light" : "Dark"')
s=s.replace('theme === "slate" ? "DARK SLATE" : "PITCH BLACK"', 'theme === "dark" ? "DARK" : "LIGHT"')
s=s.replace('theme === "slate" ? <Moon size={15} /> : <Sun size={15} />', 'theme === "dark" ? <Moon size={15} /> : <Sun size={15} />')
s=s.replace('const [theme, setTheme] = useState<"slate" | "pitch">(() => (localStorage.getItem("tech-shift-theme") as "slate" | "pitch") || "slate");', 'const [theme, setTheme] = useState<"dark" | "light">(() => { const saved = localStorage.getItem("tech-shift-theme"); return saved === "light" || saved === "pitch" ? "light" : "dark"; });')
s=s.replace('setTheme((current) => current === "slate" ? "pitch" : "slate")', 'setTheme((current) => current === "dark" ? "light" : "dark")')
s=s.replace('className={`site-shell theme-${theme}`}', 'className={`site-shell theme-${theme}`}')
p.write_text(s)
css=Path('/home/ubuntu/tech-shift/client/src/index.css')
c=css.read_text()
c += '''

/* Final robust theme contract: all visual surfaces inherit from root data-theme. */
:root[data-theme="dark"] { --bg-main: #0B0F17; --bg-surface: #151C28; --bg-surface-hover: #1E293B; --border-color: #2D3748; --text-primary: #F8FAFC; --text-secondary: #94A3B8; --text-muted: #64748B; --accent-cyan: #00F0FF; --accent-violet: #A855F7; --accent-red: #EF4444; }
:root[data-theme="light"] { --bg-main: #F8FAFC; --bg-surface: #FFFFFF; --bg-surface-hover: #F1F5F9; --border-color: #E2E8F0; --text-primary: #0F172A; --text-secondary: #334155; --text-muted: #64748B; --accent-cyan: #0284C7; --accent-violet: #7C3AED; --accent-red: #DC2626; }
html[data-theme] body, html[data-theme] .site-shell { background: var(--bg-main); color: var(--text-primary); transition: background-color .24s ease, color .24s ease; }
html[data-theme] .site-nav { background: color-mix(in srgb, var(--bg-main) 91%, transparent); border-color: var(--border-color); }
html[data-theme] .section-tinted, html[data-theme] .dark-section, html[data-theme] .dark-section-muted, html[data-theme] .final-blackout { background: var(--bg-main); color: var(--text-primary); }
html[data-theme] .hero { background-color: var(--bg-main); }
html[data-theme] .accordion-card, html[data-theme] .factor-detail, html[data-theme] .ai-field-card, html[data-theme] .coffee-table, html[data-theme] .shift-card, html[data-theme] .frontier-card, html[data-theme] .job-card, html[data-theme] .cause-card, html[data-theme] .resilience-card, html[data-theme] .manifest-card, html[data-theme] .era-card, html[data-theme] .agent-compare-card, html[data-theme] .hardware-grid article { background: var(--bg-surface); border-color: var(--border-color); color: var(--text-primary); }
html[data-theme] .accordion-card:hover, html[data-theme] .accordion-card.open, html[data-theme] .cause-card:hover, html[data-theme] .cause-card.open, html[data-theme] .shift-card.open { background: var(--bg-surface-hover); }
html[data-theme] .hero-bottom p, html[data-theme] .section-heading p, html[data-theme] .accordion-body p, html[data-theme] .cause-summary, html[data-theme] .cause-expand p, html[data-theme] .shift-body > p, html[data-theme] .frontier-card p, html[data-theme] .job-card p, html[data-theme] .resilience-card p, html[data-theme] .ai-field-card p, html[data-theme] .coffee-row p, html[data-theme] .era-card p, html[data-theme] .agent-compare-card p, html[data-theme] .hardware-grid p, html[data-theme] .embodiment-copy p { color: var(--text-secondary); }
html[data-theme] .hero-title, html[data-theme] .dark-title, html[data-theme] .section-heading h2, html[data-theme] .accordion-card strong, html[data-theme] .cause-card strong, html[data-theme] .shift-card strong, html[data-theme] .frontier-card h3, html[data-theme] .job-card h3, html[data-theme] .resilience-card h3, html[data-theme] .era-card h3, html[data-theme] .agent-compare-card h3, html[data-theme] .hardware-grid h3, html[data-theme] .embodiment-copy h3 { color: var(--text-primary); }
html[data-theme="light"] .hero-grid, html[data-theme="light"] .future-scanlines, html[data-theme="light"] .dark-vignette { opacity: .08; }
html[data-theme="light"] .hero-title em, html[data-theme="light"] .dark-title em { -webkit-text-stroke-color: color-mix(in srgb, var(--text-primary) 46%, transparent); }
html[data-theme] .coffee-row, html[data-theme] .accordion-body, html[data-theme] .cause-expand, html[data-theme] .agent-compare-card li { border-color: var(--border-color); }
html[data-theme] .theme-toggle { border-color: var(--border-color); background: var(--bg-surface); color: var(--text-primary); }
html[data-theme="light"] .theme-toggle:hover { border-color: var(--accent-cyan); color: var(--accent-cyan); }
html[data-theme="light"] .stats-strip { background: var(--bg-surface); border-color: var(--border-color); }
html[data-theme="light"] .stats-strip > div { border-color: var(--border-color); }
html[data-theme="light"] .stats-strip span, html[data-theme="light"] .mono, html[data-theme="light"] .eyebrow { color: var(--text-muted); }
html[data-theme="light"] .transition-cta, html[data-theme="light"] .agent-scenario, html[data-theme="light"] .plain-note { background: var(--bg-surface); border-color: var(--border-color); }
html[data-theme="light"] .site-footer { border-color: var(--border-color); color: var(--text-secondary); }
'''
css.write_text(c)
