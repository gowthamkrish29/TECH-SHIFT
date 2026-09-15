from pathlib import Path
p=Path('/home/ubuntu/tech-shift/client/src/pages/Home.tsx')
s=p.read_text()
s=s.replace('  Layers3, LockKeyhole, Network, Radio, Server, ShieldCheck, Sparkles, Terminal, Wifi, Workflow,', '  Layers3, LockKeyhole, Network, Radio, Server, ShieldCheck, Sparkles, Terminal, Wifi, Workflow, Moon, Sun,')
s=s.replace('function Nav({ view, navigate, progress }: { view: View; navigate: (view: View) => void; progress: number }) { return <header className="site-nav">', 'function Nav({ view, navigate, progress, theme, toggleTheme }: { view: View; navigate: (view: View) => void; progress: number; theme: "slate" | "pitch"; toggleTheme: () => void }) { return <header className="site-nav">')
s=s.replace('<div className="nav-status"><span className="pulse-dot" /><span className="mono">4 MIN READ / {Math.round(progress)}%</span></div></header>; }', '<div className="nav-status"><span className="pulse-dot" /><span className="mono">4 MIN READ / {Math.round(progress)}%</span><button className="theme-toggle" onClick={toggleTheme} aria-label={`Switch to ${theme === "slate" ? "Pitch Black" : "Dark Slate"}`} title={`Theme: ${theme === "slate" ? "Dark Slate" : "Pitch Black"}`}><span className="theme-icon">{theme === "slate" ? <Moon size={15} /> : <Sun size={15} />}</span><span className="theme-label">THEME: {theme === "slate" ? "DARK SLATE" : "PITCH BLACK"}</span></button></div></header>; }')
s=s.replace('  const [progress, setProgress] = useState(0);', '  const [progress, setProgress] = useState(0);\n  const [theme, setTheme] = useState<"slate" | "pitch">(() => (localStorage.getItem("tech-shift-theme") as "slate" | "pitch") || "slate");')
s=s.replace('  useEffect(() => { const onScroll', '  useEffect(() => { document.documentElement.dataset.theme = theme; localStorage.setItem("tech-shift-theme", theme); }, [theme]);\n  useEffect(() => { const onScroll')
s=s.replace('  return <div className="site-shell"><Nav view={view} navigate={navigate} progress={progress} />', '  return <div className={`site-shell theme-${theme}`}><Nav view={view} navigate={navigate} progress={progress} theme={theme} toggleTheme={() => setTheme((current) => current === "slate" ? "pitch" : "slate")} />')
p.write_text(s)

css=Path('/home/ubuntu/tech-shift/client/src/index.css')
c=css.read_text()
c += '''

/* Dual theme engine */
:root { --ui-bg: #0f172a; --ui-surface: #1e293b; --ui-border: #334155; --ui-text: #f8fafc; }
html[data-theme="slate"] { background: var(--ui-bg); }
html[data-theme="pitch"] { --ui-bg: #000; --ui-surface: #0a0a0a; --ui-border: #262626; --ui-text: #fff; background: #000; }
html[data-theme="pitch"] body, html[data-theme="pitch"] .site-shell { background: #000; }
html[data-theme="pitch"] .site-nav, html[data-theme="pitch"] .accordion-card, html[data-theme="pitch"] .cause-card, html[data-theme="pitch"] .resilience-card, html[data-theme="pitch"] .manifest-card, html[data-theme="pitch"] .era-card, html[data-theme="pitch"] .agent-compare-card, html[data-theme="pitch"] .hardware-grid article, html[data-theme="pitch"] .job-card, html[data-theme="pitch"] .frontier-card, html[data-theme="pitch"] .shift-card { background: #0a0a0a; border-color: #262626; }
html[data-theme="slate"] .site-nav { background: rgba(15,23,42,.88); }
.theme-toggle { display: inline-flex; align-items: center; gap: 7px; min-height: 32px; padding: 7px 10px; border: 1px solid var(--ui-border); background: color-mix(in srgb, var(--ui-surface) 76%, transparent); color: var(--ui-text); font: 10px var(--mono); letter-spacing: .05em; transition: border-color .2s, color .2s, transform .16s var(--ease-out); }
.theme-toggle:hover { border-color: var(--cyan); color: var(--cyan); transform: translateY(-1px); }.theme-toggle:active { transform: scale(.97); }.theme-icon { display: grid; place-items: center; }.theme-label { white-space: nowrap; }
.nav-status { flex-wrap: wrap; justify-content: flex-end; }
/* Large reading scale */
.hero-bottom p { font-size: 22px; line-height: 1.75; max-width: 700px; }
.section-heading h2 { font-size: clamp(36px, 4.2vw, 52px); }
.section-heading p { max-width: 760px; font-size: 20px; line-height: 1.75; }
.accordion-card strong, .cause-card strong, .shift-card strong, .frontier-card h3, .job-card h3, .resilience-card h3 { font-size: 26px; }
.accordion-body p, .cause-summary, .cause-expand p, .shift-body > p, .frontier-card p, .job-card p, .resilience-card p, .ai-field-card p, .coffee-row p, .era-card p, .agent-compare-card p, .hardware-grid p { font-size: 18px; line-height: 1.75; }
.cause-summary { max-width: 700px; }
@media (max-width: 760px) { .theme-label { display: none; }.theme-toggle { padding: 8px; }.hero-bottom p { font-size: 20px; }.section-heading p { font-size: 18px; }.accordion-card strong, .cause-card strong, .shift-card strong, .frontier-card h3, .job-card h3, .resilience-card h3 { font-size: 24px; } }
'''
css.write_text(c)
