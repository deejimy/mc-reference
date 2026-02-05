import re

# Lire glossary_ref.txt
with open('.work/glossary_ref.txt', 'r', encoding='utf-8') as f:
    ref_lines = [l.strip() for l in f if l.strip()]

# Extraire les termes français 
ref_terms = set()
for entry in ref_lines:
    if '=' in entry:
        fr_term = entry.split('=')[0].strip().strip('"')
        ref_terms.add(fr_term.lower())

print('GLOSSARY_REF.TXT: ' + str(len(ref_lines)) + ' entrées')

# Lire Glossaire.md et extraire affichages
with open('docs/Glossaire/Glossaire.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

wiki_pattern = r'\[\[([^\]|]+)\|?([^\]]*)\]\]'
matches = re.findall(wiki_pattern, md_content)

md_terms = set()
for file_ref, display in matches:
    # Ignorer les liens vers des images
    if file_ref.endswith(('.jpg', '.png', '.gif', '.svg')):
        continue
    term = display if display else file_ref
    term = term.strip('"').strip('« »')  # Ignorer les guillemets
    if term:  # Ignorer les termes vides
        md_terms.add(term.lower())

print('GLOSSAIRE.MD: ' + str(len(matches)) + ' entrées')

only_in_ref = ref_terms - md_terms
only_in_glossaire = md_terms - ref_terms

max = 300
print('\n=== UNIQUEMENT dans glossary_ref.txt: ' + str(len(only_in_ref)) + ' ===')
for term in sorted(list(only_in_ref))[:max]:
    print('  ' + term)
if len(only_in_ref) > max:
    print('  ... et ' + str(len(only_in_ref) - max) + ' autres')

print('\n=== UNIQUEMENT dans Glossaire.md: ' + str(len(only_in_glossaire)) + ' ===')
for term in sorted(list(only_in_glossaire))[:max]:
    print('  ' + term)
if len(only_in_glossaire) > max:
    print('  ... et ' + str(len(only_in_glossaire) - max) + ' autres')

print('\n=== Résumé ===')
print('Entrées communes: ' + str(len(ref_terms & md_terms)))
