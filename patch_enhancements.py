from pathlib import Path

p = Path('/home/ubuntu/tech-shift/client/src/pages/Home.tsx')
s = p.read_text()

s = s.replace('const navItems: NavItem[] = [\n  { id: "now", index: "01", label: "NOW" },\n  { id: "future", index: "02", label: "2030" },\n  { id: "dark", index: "03", label: "DARK SIDE" },\n];', '''const navItems: NavItem[] = [
  { id: "now", index: "01", label: "NOW" },
  { id: "future", index: "02", label: "2030" },
  { id: "dark", index: "03", label: "DARK SIDE" },
];

function queryValue(key: string, fallback: string) {
  return new URLSearchParams(window.location.search).get(key) || fallback;
}

function updateDeepLink(view: View, values: Record<string, string | number> = {}) {
  const url = new URL(window.location.href);
  url.hash = view;
  Object.entries(values).forEach(([key, value]) => url.searchParams.set(key, String(value)));
  window.history.replaceState(null, "", `${url.pathname}${url.search}${url.hash}`);
}

function sectionLink(view: View, section: string, values: Record<string, string | number> = {}) {
  updateDeepLink(view, { section, ...values });
}''')

s = s.replace('const [activeYear, setActiveYear] = useState("NOW");\n  const [activeTech, setActiveTech] = useState("AI");', 'const [activeYear, setActiveYear] = useState(() => queryValue("year", "NOW"));\n  const [activeTech, setActiveTech] = useState(() => queryValue("layer", "AI"));')
s = s.replace('onClick={() => setActiveTech(name === "Cloud computing" ? "Cloud" : name === "Big data" ? "Data" : "AI")}', 'onClick={() => { const layer = name === "Cloud computing" ? "Cloud" : name === "Big data" ? "Data" : "AI"; setActiveTech(layer); sectionLink("now", "explore", { layer }); }}')
s = s.replace('onClick={() => setActiveYear(year)}', 'onClick={() => { setActiveYear(year); sectionLink("now", "race", { year }); }}')
s = s.replace('onClick={() => setActiveTech(item)}', 'onClick={() => { setActiveTech(item); sectionLink("now", "map", { layer: item }); }}')

s = s.replace('<button key={year} className={`timeline-item ${activeYear === year ? "selected" : ""}`} onClick={() => { setActiveYear(year); sectionLink("now", "race", { year }); }}><span className="timeline-dot" /><span className="timeline-year mono">{year}</span><strong>{title}</strong><small>{note}</small></button>', '<button key={year} className={`timeline-item ${activeYear === year ? "selected" : ""}`} onClick={() => { setActiveYear(year); sectionLink("now", "race", { year }); }} aria-label={`${year}: ${title}`}><span className="timeline-dot" /><span className="timeline-year mono">{year}</span><strong>{title}</strong><small>{note}</small><span className="timeline-tooltip" role="tooltip">{note}</span></button>')

s = s.replace('const [filter, setFilter] = useState("ALL"); const [selectedRole, setSelectedRole] = useState(2);', 'const [filter, setFilter] = useState(() => queryValue("filter", "ALL")); const [selectedRole, setSelectedRole] = useState(() => Number(queryValue("role", "2")));')
s = s.replace('onClick={() => setFilter(item)}', 'onClick={() => { setFilter(item); sectionLink("future", "emerging", { filter: item }); }}')
s = s.replace('onClick={() => setSelectedRole(i)}', 'onClick={() => { setSelectedRole(i); sectionLink("future", "roles", { role: i }); }}')

s = s.replace('const [activeHorizon, setActiveHorizon] = useState("1 DAY");', 'const [activeHorizon, setActiveHorizon] = useState(() => queryValue("horizon", "1 DAY"));')
s = s.replace('onClick={() => setActiveHorizon(time)}', 'onClick={() => { setActiveHorizon(time); sectionLink("dark", "horizons", { horizon: time }); }}')

s = s.replace('const hash = window.location.hash.replace("#", "") as View; return ["now", "future", "dark"].includes(hash) ? hash : "now";', 'const hash = window.location.hash.replace("#", "") as View; return ["now", "future", "dark"].includes(hash) ? hash : "now";')
s = s.replace('window.scrollTo({ top: 0, behavior: "instant" as ScrollBehavior }); document.body.dataset.view = view;', 'window.scrollTo({ top: 0, behavior: "instant" as ScrollBehavior }); document.body.dataset.view = view; const section = queryValue("section", ""); if (section) window.setTimeout(() => document.getElementById(section)?.scrollIntoView({ behavior: "smooth", block: "start" }), 90);')
s = s.replace('const navigate = (next: View) => { setView(next); window.history.replaceState(null, "", `#${next}`);', 'const navigate = (next: View) => { setView(next); updateDeepLink(next);')

# Add section anchors to major future/dark sections.
s = s.replace('<section className="section container"><SectionHeading index="01 / 06" kicker="The 2030 stack"', '<section className="section container" id="stack"><SectionHeading index="01 / 06" kicker="The 2030 stack"')
s = s.replace('<section className="section section-tinted"><div className="container"><SectionHeading index="02 / 06" kicker="AI agents + intent-driven systems"', '<section className="section section-tinted" id="agents"><div className="container"><SectionHeading index="02 / 06" kicker="AI agents + intent-driven systems"')
s = s.replace('<section className="section container"><SectionHeading index="03 / 06" kicker="The next programming language"', '<section className="section container" id="intent"><SectionHeading index="03 / 06" kicker="The next programming language"')
s = s.replace('<section className="section section-tinted"><div className="container"><SectionHeading index="04 / 06" kicker="Emerging tech wall"', '<section className="section section-tinted" id="emerging"><div className="container"><SectionHeading index="04 / 06" kicker="Emerging tech wall"')
s = s.replace('<section className="section container"><SectionHeading index="05 / 06" kicker="Evolving roles"', '<section className="section container" id="roles"><SectionHeading index="05 / 06" kicker="Evolving roles"')
s = s.replace('<section className="section dark-section"><div className="container"><SectionHeading index="01 / 06" kicker="The first 24 hours"', '<section className="section dark-section" id="first-hours"><div className="container"><SectionHeading index="01 / 06" kicker="The first 24 hours"')
s = s.replace('<section className="section dark-section dark-section-muted"><div className="container"><SectionHeading index="02 / 06" kicker="Critical failures"', '<section className="section dark-section dark-section-muted" id="failures"><div className="container"><SectionHeading index="02 / 06" kicker="Critical failures"')
s = s.replace('<section className="section dark-section"><div className="container"><SectionHeading index="03 / 06" kicker="The cascade"', '<section className="section dark-section" id="cascade"><div className="container"><SectionHeading index="03 / 06" kicker="The cascade"')
s = s.replace('<section className="section dark-section dark-section-muted"><div className="container"><SectionHeading index="04 / 06" kicker="Survival horizons"', '<section className="section dark-section dark-section-muted" id="horizons"><div className="container"><SectionHeading index="04 / 06" kicker="Survival horizons"')
s = s.replace('<section className="section dark-section"><div className="container"><SectionHeading index="05 / 06" kicker="Rebuilding civilizations"', '<section className="section dark-section" id="rebuilding"><div className="container"><SectionHeading index="05 / 06" kicker="Rebuilding civilizations"')
s = s.replace('<section className="section manifest-section"><div className="container">', '<section className="section manifest-section" id="manifest"><div className="container">')

p.write_text(s)

css = Path('/home/ubuntu/tech-shift/client/src/index.css')
styles = css.read_text()
styles += '''

/* Ambient narrative motion */
.hero-now .hero-grid { animation: grid-breathe 14s ease-in-out infinite alternate; }
.hero-now .orbit-one { animation: orbit-drift 18s ease-in-out infinite alternate; }
.hero-now .orbit-two { animation: orbit-drift 24s ease-in-out -5s infinite alternate-reverse; }
.hero-future .future-scanlines { animation: scan-drift 8s linear infinite; }
.hero-future::after { content: ""; position: absolute; inset: 18% 4% auto auto; width: 260px; height: 260px; border: 1px solid rgba(199,255,74,.18); border-radius: 50%; box-shadow: 0 0 80px rgba(199,255,74,.12); animation: future-pulse 5s ease-in-out infinite; pointer-events: none; }
.hero-dark .dark-vignette { animation: dark-breathe 7s ease-in-out infinite alternate; }
.hero-dark::after { content: ""; position: absolute; inset: 0; opacity: .12; pointer-events: none; background-image: repeating-linear-gradient(0deg, transparent 0 4px, rgba(255,79,73,.14) 5px, transparent 6px); mix-blend-mode: screen; animation: signal-jitter 11s steps(2, end) infinite; }

@keyframes grid-breathe { from { transform: translate3d(0,0,0) scale(1); opacity: .34; } to { transform: translate3d(-18px, 12px, 0) scale(1.04); opacity: .52; } }
@keyframes orbit-drift { from { transform: rotate(-19deg) translate3d(0,0,0); } to { transform: rotate(-13deg) translate3d(-24px, 18px, 0); } }
@keyframes scan-drift { from { background-position: 0 0; } to { background-position: 0 72px; } }
@keyframes future-pulse { 0%, 100% { transform: scale(.88); opacity: .35; } 50% { transform: scale(1.15); opacity: .8; } }
@keyframes dark-breathe { from { opacity: .58; transform: scale(1); } to { opacity: .88; transform: scale(1.08); } }
@keyframes signal-jitter { 0%, 90%, 100% { transform: translate(0); opacity: .08; } 92% { transform: translate(2px, -1px); opacity: .22; } 94% { transform: translate(-1px, 1px); opacity: .14; } }

/* Timeline hover context */
.timeline-item { isolation: isolate; }
.timeline-item::after { content: ""; position: absolute; left: 0; right: 12px; top: 21px; height: 36px; border: 1px solid transparent; transition: border-color .2s, background .2s, transform .2s; pointer-events: none; }
.timeline-item:hover::after, .timeline-item:focus-visible::after, .timeline-item.selected::after { border-color: rgba(118,242,229,.38); background: rgba(118,242,229,.035); transform: translateY(-4px); }
.timeline-tooltip { position: absolute; z-index: 5; left: 0; top: -54px; width: max-content; max-width: 190px; padding: 8px 10px; border: 1px solid rgba(118,242,229,.42); background: #0b1111; color: #b7c8c6; font: 10px/1.4 var(--mono); opacity: 0; transform: translateY(5px); pointer-events: none; transition: opacity .18s, transform .18s; box-shadow: 0 12px 28px rgba(0,0,0,.28); }
.timeline-tooltip::after { content: ""; position: absolute; left: 14px; bottom: -5px; width: 8px; height: 8px; background: #0b1111; border-right: 1px solid rgba(118,242,229,.42); border-bottom: 1px solid rgba(118,242,229,.42); transform: rotate(45deg); }
.timeline-item:hover .timeline-tooltip, .timeline-item:focus-visible .timeline-tooltip, .timeline-item.selected .timeline-tooltip { opacity: 1; transform: none; }

@media (max-width: 620px) { .timeline-tooltip { position: fixed; left: 20px; right: 20px; top: auto; bottom: 20px; width: auto; max-width: none; } .timeline-tooltip::after { display: none; } .hero-future::after { width: 160px; height: 160px; right: -70px; } }
@media (prefers-reduced-motion: reduce) { .hero-now .hero-grid, .hero-now .orbit-one, .hero-now .orbit-two, .hero-future .future-scanlines, .hero-future::after, .hero-dark .dark-vignette, .hero-dark::after { animation: none; } }
'''
css.write_text(styles)
