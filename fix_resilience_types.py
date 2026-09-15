from pathlib import Path
p=Path('/home/ubuntu/tech-shift/client/src/pages/Home.tsx')
s=p.read_text().replace('const antifragility = [[', 'const antifragility: [string, string, string][] = [[')
p.write_text(s)
