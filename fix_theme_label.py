from pathlib import Path
p=Path('/home/ubuntu/tech-shift/client/src/pages/Home.tsx')
s=p.read_text().replace('theme === "slate" ? "Dark Slate" : "Pitch Black"', 'theme === "dark" ? "Dark" : "Light"')
p.write_text(s)
