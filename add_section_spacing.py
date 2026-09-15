from pathlib import Path
p=Path('/home/ubuntu/tech-shift/client/src/index.css')
s=p.read_text()
s += '''

/* DARK SIDE vertical rhythm: keep each narrative module visually distinct */
.dark-section + .dark-section { padding-top: 150px; }
#reversion .manual-ladder { margin-bottom: 145px; }
#reversion .section-heading + .manual-ladder { margin-top: 18px; }
#resilience { padding-top: 170px; }
#resilience .antifragility-grid { margin-top: 26px; }
#resilience .realization-banner { margin-top: 56px; }
.final-blackout { margin-top: 110px; padding-top: 170px; }
@media (max-width: 620px) { .dark-section + .dark-section { padding-top: 105px; } #reversion .manual-ladder { margin-bottom: 95px; } #resilience { padding-top: 110px; } #resilience .realization-banner { margin-top: 38px; } .final-blackout { margin-top: 70px; padding-top: 110px; } }
'''
p.write_text(s)
