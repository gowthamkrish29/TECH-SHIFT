from pathlib import Path
p=Path('/home/ubuntu/tech-shift/client/src/pages/Home.tsx')
s=p.read_text()
replacements={
'"Redundancy",':'"🔄 Redundancy",',
'"Offline + air-gapped backups",':'"💾 Offline Backups",',
'"Alternative + analog communication",':'"📡 Alternative Communication",',
'"Resilient + microgrid power",':'"⚡ Resilient Power",',
'"Human + manual skills",':'"👨‍🔧 Human Skills",',
'"Hardened cyber-physical security",':'"🛡️ Cybersecurity",',
'"Responsible AI + oversight",':'"🤖 Responsible AI",',
'"Radical decentralization",':'"🌍 Decentralization",',
}
for a,b in replacements.items():
    s=s.replace(a,b)
p.write_text(s)
css=Path('/home/ubuntu/tech-shift/client/src/index.css')
c=css.read_text()
c += '''

/* Distinct solution cards: each principle gets its own visual signal */
.antifragility-card { position: relative; overflow: hidden; border-width: 1px; background: linear-gradient(145deg, var(--card-bg), var(--bg-surface) 72%); border-color: var(--card-border); }.antifragility-card::before { content: ""; position: absolute; inset: 0 0 auto; height: 4px; background: var(--card-accent); }.antifragility-card:nth-child(1) { --card-accent: #22D3EE; --card-border: rgba(34,211,238,.55); --card-bg: rgba(34,211,238,.16); }.antifragility-card:nth-child(2) { --card-accent: #A78BFA; --card-border: rgba(167,139,250,.55); --card-bg: rgba(167,139,250,.16); }.antifragility-card:nth-child(3) { --card-accent: #60A5FA; --card-border: rgba(96,165,250,.55); --card-bg: rgba(96,165,250,.16); }.antifragility-card:nth-child(4) { --card-accent: #FBBF24; --card-border: rgba(251,191,36,.6); --card-bg: rgba(251,191,36,.15); }.antifragility-card:nth-child(5) { --card-accent: #FB923C; --card-border: rgba(251,146,60,.6); --card-bg: rgba(251,146,60,.15); }.antifragility-card:nth-child(6) { --card-accent: #F87171; --card-border: rgba(248,113,113,.6); --card-bg: rgba(248,113,113,.15); }.antifragility-card:nth-child(7) { --card-accent: #C084FC; --card-border: rgba(192,132,252,.6); --card-bg: rgba(192,132,252,.15); }.antifragility-card:nth-child(8) { --card-accent: #34D399; --card-border: rgba(52,211,153,.6); --card-bg: rgba(52,211,153,.15); }.antifragility-card .antifragility-icon { border-color: var(--card-accent); color: var(--card-accent); background: color-mix(in srgb, var(--card-accent) 16%, transparent); }.antifragility-card h3 { min-height: 50px; color: var(--card-accent); font-size: 22px; }.antifragility-card strong { color: var(--text-primary); }.antifragility-card p { color: var(--text-secondary); }.antifragility-card > span { color: var(--card-accent); }.antifragility-card:hover { border-color: var(--card-accent); box-shadow: 0 16px 34px color-mix(in srgb, var(--card-accent) 18%, transparent); }
html[data-theme="light"] .antifragility-card { background: linear-gradient(145deg, var(--card-bg), #fff 72%); box-shadow: 0 8px 20px rgba(15,23,42,.08); }.antifragility-card h3 { letter-spacing: -.02em; }
'''
css.write_text(c)
