#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script combiné pour :
1. Rejoindre les lignes mal coupées
2. Ajouter des lignes vides avant les titres en MAJUSCULES
"""

import re

input_file = '../docs/Appendice/VI.md'
output_file = '../docs/Appendice/VI_cleaned.md'


def is_uppercase_line(line):
    """Vérifie si une ligne est un titre (entièrement en majuscules)"""
    stripped = line.strip()
    if not stripped:
        return False
    letters = ''.join(c for c in stripped if c.isalpha())
    return letters.isupper() and len(letters) >= 2


def should_join_with_previous(current_line, previous_line):
    """
    Détermine si la ligne actuelle devrait être jointe avec la précédente.
    """
    current = current_line.strip()
    previous = previous_line.strip()
    
    if not current or not previous:
        return False
    
    # Ne pas joindre si la ligne actuelle est un titre
    if is_uppercase_line(current):
        return False
    
    # Ne pas joindre si la ligne actuelle commence par une puce
    bullet_patterns = [r'^[•\-\*→»]', r'^\d+\.', r'^[a-z]\)']
    for pattern in bullet_patterns:
        if re.match(pattern, current):
            return False
    
    # Joindre si la ligne actuelle commence par une minuscule
    if current[0].islower():
        return True
    
    # Ne pas joindre si la ligne précédente se termine par une ponctuation forte
    strong_endings = ['.', ':', '—', '–', '»', '"', '"']
    if any(previous.endswith(ending) for ending in strong_endings):
        # Exception : continuation évidente
        if current and current[0].islower():
            return True
        return False
    
    # Joindre si la ligne précédente se termine par une virgule
    if previous.endswith(','):
        return True
    
    # Joindre si pas de ponctuation de fin
    if not any(previous.endswith(p) for p in ['.', '!', '?', ':', ';']):
        return True
    
    return False


def process_file(content):
    """
    Traite le fichier en deux étapes :
    1. Rejoint les lignes mal coupées
    2. Ajoute des lignes vides avant les titres
    """
    lines = content.split('\n')
    
    # ÉTAPE 1 : Rejoindre les lignes mal coupées
    print("Étape 1 : Rejoindre les lignes mal coupées...")
    fixed_lines = []
    i = 0
    
    while i < len(lines):
        current_line = lines[i]
        
        # Ligne vide ou titre : garder tel quel
        if not current_line.strip() or is_uppercase_line(current_line):
            fixed_lines.append(current_line)
            i += 1
            continue
        
        # Construire la ligne complète
        complete_line = current_line
        j = i + 1
        
        while j < len(lines):
            next_line = lines[j]
            if not next_line.strip():
                break
            
            if should_join_with_previous(next_line, complete_line):
                complete_line = complete_line.rstrip() + ' ' + next_line.lstrip()
                j += 1
            else:
                break
        
        fixed_lines.append(complete_line)
        i = j if j > i + 1 else i + 1
    
    print(f"  Lignes avant: {len(lines)}")
    print(f"  Lignes après: {len(fixed_lines)}")
    print(f"  Lignes rejointes: {len(lines) - len(fixed_lines)}")
    
    # ÉTAPE 2 : Ajouter des lignes vides avant les titres en MAJUSCULES
    print("\nÉtape 2 : Ajouter des lignes vides avant les titres...")
    final_lines = []
    titles_found = 0
    
    for i, line in enumerate(fixed_lines):
        if is_uppercase_line(line):
            # Ajouter ligne vide avant (sauf si première ligne ou déjà une ligne vide)
            if (
                i > 0
                and final_lines
                and final_lines[-1].strip()
                and not is_uppercase_line(fixed_lines[i - 1])
            ):
                final_lines.append('')
                titles_found += 1
        final_lines.append(line)
    
    print(f"  Titres trouvés: {titles_found}")
    print(f"  Lignes finales: {len(final_lines)}")
    
    return '\n'.join(final_lines)


def show_examples(original_content, fixed_content):
    """Affiche quelques exemples de corrections"""
    orig_lines = original_content.split('\n')
    fixed_lines = fixed_content.split('\n')
    
    print("\n" + "="*70)
    print("EXEMPLES DE CORRECTIONS")
    print("="*70)
    
    # Trouver des exemples où des lignes ont été rejointes
    examples = 0
    for i, fixed_line in enumerate(fixed_lines):
        if not fixed_line.strip():
            continue
        
        # Chercher dans l'original
        if examples < 3 and len(fixed_line) > 100:
            # Ligne longue = probablement une fusion
            search_text = fixed_line[:30]
            for j, orig_line in enumerate(orig_lines):
                if search_text in orig_line:
                    examples += 1
                    print(f"\nExemple {examples}:")
                    print("AVANT:")
                    # Afficher quelques lignes autour
                    for k in range(max(0, j-1), min(len(orig_lines), j+3)):
                        if orig_lines[k].strip():
                            prefix = "→ " if k == j else "  "
                            print(f"  {prefix}{orig_lines[k][:65]}")
                    
                    print("APRÈS:")
                    print(f"  → {fixed_line[:65]}")
                    if len(fixed_line) > 65:
                        print(f"    {fixed_line[65:130]}")
                    break
    
    # Trouver des exemples de titres avec ligne vide ajoutée
    print("\n" + "-"*70)
    print("TITRES AVEC LIGNE VIDE AJOUTÉE:")
    print("-"*70)
    title_examples = 0
    for i, line in enumerate(fixed_lines):
        if is_uppercase_line(line) and title_examples < 5:
            if i > 0 and not fixed_lines[i-1].strip():
                title_examples += 1
                print(f"\n  Ligne {i-1}: [ligne vide]")
                print(f"  Ligne {i}: {line}")


def main():
    print("="*70)
    print("NETTOYAGE COMPLET DU FICHIER")
    print("="*70)
    print(f"\nFichier source: {input_file}")
    print(f"Fichier sortie: {output_file}")
    
    # Lire le fichier
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"\nLignes dans le fichier original: {len(content.split(chr(10)))}")
    
    # Traiter le fichier
    print("\n" + "="*70)
    fixed_content = process_file(content)
    
    # Enregistrer
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print("\n" + "="*70)
    print(f"✓ Fichier enregistré: {output_file}")
    
    # Afficher des exemples
    show_examples(content, fixed_content)
    
    print("\n" + "="*70)
    print("TERMINÉ !")
    print("="*70)


if __name__ == '__main__':
    main()