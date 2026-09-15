from pathlib import Path
p=Path('/home/ubuntu/tech-shift/client/src/index.css')
s=p.read_text()
s += '''

/* Light-theme outage timeline contrast */
html[data-theme="light"] .outage-step { border-color: #94A3B8; background: #FFFFFF; color: #0F172A; }
html[data-theme="light"] .outage-step:hover, html[data-theme="light"] .outage-step:focus-visible { border-color: #B91C1C; background: #FFF1F2; box-shadow: 0 8px 22px rgba(185,28,28,.14); }
html[data-theme="light"] .outage-step.selected { border: 2px solid #B91C1C; background: #FEE2E2; box-shadow: inset 4px 0 0 #B91C1C, 0 8px 22px rgba(185,28,28,.16); }
html[data-theme="light"] .outage-step strong { color: #450A0A !important; font-weight: 700; }
html[data-theme="light"] .outage-step small { color: #7F1D1D !important; font-weight: 500; }
html[data-theme="light"] .outage-step > span:nth-child(2) { color: #991B1B !important; font-weight: 700; }
html[data-theme="light"] .outage-dot { border-color: #B91C1C; }
html[data-theme="light"] .outage-step.selected .outage-dot { background: #B91C1C; border-color: #B91C1C; }
html[data-theme="light"] .outage-tooltip { border-color: #B91C1C; background: #450A0A; color: #FFFFFF; box-shadow: 0 8px 18px rgba(69,10,10,.22); }
html[data-theme="light"] .outage-readout { border: 2px solid #B91C1C; background: #FFF7F7; box-shadow: 0 8px 20px rgba(185,28,28,.10); }
html[data-theme="light"] .outage-readout > span { color: #991B1B !important; font-weight: 700; }
html[data-theme="light"] .outage-readout h3 { color: #450A0A !important; font-weight: 700; }
html[data-theme="light"] .outage-readout p { color: #7F1D1D !important; font-weight: 500; }
html[data-theme="high"] .outage-step, html[data-contrast="high"] .outage-step { border-color: var(--border-color); }
html[data-contrast="high"] .outage-step:hover, html[data-contrast="high"] .outage-step.selected { border-color: var(--accent-red); background: var(--accent-red-bg, #FEE2E2); }
html[data-contrast="high"] .outage-step strong, html[data-contrast="high"] .outage-step small, html[data-contrast="high"] .outage-readout h3, html[data-contrast="high"] .outage-readout p { color: var(--text-primary) !important; }
'''
p.write_text(s)
