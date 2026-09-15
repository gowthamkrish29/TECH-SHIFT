from pathlib import Path
p=Path('/home/ubuntu/tech-shift/client/src/pages/Home.tsx')
s=p.read_text()
s=s.replace('const [openCause, setOpenCause] = useState(() => Number(q("cause", "0")));', 'const [openCause, setOpenCause] = useState(() => { const raw = Number(q("cause", q("pillar", "0"))); return Number.isFinite(raw) && raw >= 0 && raw < vulnerabilities.length ? raw : 0; });')
s=s.replace('jump("dark", "vulnerability", { cause: i });', 'jump("dark", "vulnerability", { cause: i, pillar: i });')
p.write_text(s)
