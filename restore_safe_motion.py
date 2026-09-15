from pathlib import Path
css=Path('/home/ubuntu/tech-shift/client/src/index.css')
s=css.read_text()
s += '''

/* Restored motion: transform-only card entrances keep every card visible. */
@keyframes cause-card-enter { from { transform: translateY(14px); } to { transform: translateY(0); } }
@keyframes cause-border-pulse { 0%, 100% { box-shadow: 0 0 0 rgba(239,68,68,0); } 50% { box-shadow: 0 0 26px rgba(239,68,68,.10); } }
.cause-card { opacity: 1 !important; transform: translateY(0) !important; animation: cause-card-enter .55s var(--ease-out) both; transition: transform .2s var(--ease-out), border-color .2s, box-shadow .2s; }
.cause-card:nth-child(2) { animation-delay: 55ms; }.cause-card:nth-child(3) { animation-delay: 110ms; }.cause-card:nth-child(4) { animation-delay: 165ms; }
.cause-card:hover { transform: translateY(-3px) !important; border-color: rgba(239,68,68,.55); box-shadow: 0 12px 28px rgba(0,0,0,.24); }
.cause-card.open { animation: cause-border-pulse 2.4s ease-in-out infinite; }
.cause-card.open:hover { transform: translateY(-3px) !important; }
@media (prefers-reduced-motion: reduce) { .cause-card, .cause-card.open { animation: none; } }
'''
css.write_text(s)
