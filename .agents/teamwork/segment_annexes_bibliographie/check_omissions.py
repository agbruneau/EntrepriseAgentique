keywords = [
    'Morris II', 'Comaroff', 'Cohen', 'AgentPoison', 'BadChain',
    'OWASP', 'Top 10', 'Agentic AI',
    'MetaGPT', 'ChatDev', 'AutoGen', 'Wu, Qingyun', 'Hong, Sirui',
    'Swarm', 'OpenAI Swarm',
    'Agent-as-a-Judge', 'Zheng, Lianmin',
    'Tree of Thoughts', 'Yao, Shunyu',
    'IOSCO', 'CPMI',
    'Operational Resilience', 'E-21',
    'ISO/IEC 42001', 'ISO 42001'
]

with open(r'c:\Github\EntrepriseAgentique\.agents\teamwork\segment_annexes_bibliographie\entries_index.txt', 'r', encoding='utf-8') as f:
    text = f.read()

entries = text.split('\n\n')

for kw in keywords:
    matches = [e for e in entries if kw.lower() in e.lower()]
    print(f"Keyword '{kw}': {len(matches)} matches")
    for m in matches[:2]:
        print(f"   -> {m[:100]}...")
