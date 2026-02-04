import re, os, sys
root = "docs"
md_link = re.compile(r'\[[^\]]+\]\(([^)]+\.md)\)')
bad = []
for dirpath,_,files in os.walk(root):
	for f in files:
		if f.endswith('.md'):
			p = os.path.join(dirpath,f)
			try:
				s = open(p,encoding='utf-8').read()
			except Exception:
				continue
			for m in md_link.findall(s):
				target = os.path.normpath(os.path.join(dirpath, m))
				if not os.path.exists(target):
					bad.append((p, m))
if bad:
	print("Liens cassés trouvés:")
	for src,t in bad: print(f"- {src} -> {t}")
	sys.exit(1)
print("Aucun lien cassé trouvé.")