import os
import re

# Lire Glossaire.md et extraire les references
with open('docs/Glossaire/Glossaire.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

# Extraire les fichiers referencces dans les liens wiki
wiki_pattern = r'\[\[([^\]|]+)\|?[^\]]*\]\]'
matches = re.findall(wiki_pattern, md_content)

referenced_files = set()
for match in matches:
    # Ignorer les images
    if not match.endswith(('.jpg', '.png', '.gif', '.svg')):
        referenced_files.add(match + '.md')

print('Fichiers referencces dans Glossaire.md: ' + str(len(referenced_files)))

# Lister tous les fichiers .md dans le dossier Glossaire
all_files = set()
for root, dirs, files in os.walk('docs/Glossaire'):
    for file in files:
        if file.endswith('.md') and file != 'Glossaire.md':
            all_files.add(file)

print('Fichiers .md dans le dossier: ' + str(len(all_files)))

# Trouver les fichiers non referencces
orphan_files = all_files - referenced_files

print('\n=== Fichiers NON referencces dans Glossaire.md: ' + str(len(orphan_files)) + ' ===')
for file in sorted(orphan_files):
    print('  ' + file)
