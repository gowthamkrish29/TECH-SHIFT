from pathlib import Path
p=Path('/home/ubuntu/tech-shift/client/src/pages/Home.tsx')
s=p.read_text()
s=s.replace('const agentRows = [["Current conversational AI", "PASSIVE", ["Needs constant human prompts", "Generates text answers", "Little cross-session state"]], ["2030 autonomous agent swarms", "ACTIVE + PROACTIVE", ["Self-plans and uses tools", "Agents cross-verify each other", "Humans approve high-impact edge cases"]]];', 'const agentRows: [string, string, string[]][] = [["Current conversational AI", "PASSIVE", ["Needs constant human prompts", "Generates text answers", "Little cross-session state"]], ["2030 autonomous agent swarms", "ACTIVE + PROACTIVE", ["Self-plans and uses tools", "Agents cross-verify each other", "Humans approve high-impact edge cases"]]];')
p.write_text(s)
