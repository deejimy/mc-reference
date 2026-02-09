#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour générer des fichiers .md pour chaque chapitre du glossaire.
Les chapitres sont séparés par des lignes vides et identifiés par un titre en MAJUSCULES.
"""

import re
import os
from pathlib import Path
import unicodedata

input = '../.work/v14fr.txt'
version = "**FR v1.4**:  "
output_dir = 'Glossaire_back'

def normalize_quotes(text):
    """Normalise tous les types de guillemets vers des guillemets ASCII simples."""
    # Guillemets courbes et autres variantes vers guillemets droits
    quote_chars = [
        '\u201c', '\u201d',  # " " guillemets doubles courbes
        '\u2018', '\u2019',  # ' ' guillemets simples courbes
        '\u00ab', '\u00bb',  # « » guillemets français
        '\u2039', '\u203a',  # ‹ › guillemets simples français
    ]
    for char in quote_chars:
        text = text.replace(char, '"')
    return text


def remove_accents(text):
    """Supprime les accents d'une chaîne de caractères."""
    nfd = unicodedata.normalize('NFD', text)
    return ''.join(char for char in nfd if unicodedata.category(char) != 'Mn')


def clean_filename(text):
    """
    Nettoie un texte pour en faire un nom de fichier valide:
    - Supprime les accents
    - Remplace les espaces par des underscores
    - Supprime les caractères spéciaux
    - Met en PascalCase (première lettre de chaque mot en majuscule)
    """
    # Supprimer les accents
    text = remove_accents(text)
    
    # Supprimer les guillemets et autres caractères spéciaux
    text = re.sub(r'["\',\(\)]+', '', text)
    
    # Remplacer les tirets et autres séparateurs par des espaces
    text = re.sub(r'[-_/]+', ' ', text)
    
    # Séparer en mots et mettre en PascalCase
    words = text.split()
    # Première lettre de chaque mot en majuscule, reste en minuscule
    pascal_case = ''.join(word.capitalize() for word in words if word)
    
    return pascal_case


def is_chapter_title(line):
    """
    Vérifie si une ligne est un titre de chapitre (exclusivement en MAJUSCULES).
    """
    stripped = line.strip()
    if not stripped:
        return False
    
    # Extraire tous les caractères alphabétiques
    letters = ''.join(c for c in stripped if c.isalpha())
    
    # Si pas de lettres ou moins de 3 caractères, ce n'est pas un titre
    if not letters or len(letters) < 3:
        return False
    
    # Vérifier que toutes les lettres sont en majuscules
    return letters.isupper()


def parse_glossary_ref(ref_file_path):
    """
    Parse le fichier glossary_ref.txt pour créer un dictionnaire de traduction.
    Format: Français = English
    """
    translation_dict = {}
    
    with open(ref_file_path, 'r', encoding='utf-8') as f:
        for line in f:
            # Nettoyer les retours chariots Windows et espaces
            line = line.replace('\r', '').strip()
            # Normaliser les guillemets
            line = normalize_quotes(line)
            
            if not line or '=' not in line:
                continue
            
            # Séparer français et anglais
            parts = line.split('=', 1)
            if len(parts) == 2:
                french = parts[0].strip()
                english = parts[1].strip()
                
                # Nettoyer les guillemets des deux côtés
                english_clean = english.strip().strip('"').strip()
                french_clean = french.strip().strip('"').strip()
                
                # Utiliser l'anglais en MAJUSCULES comme clé (sans les guillemets)
                english_upper = english_clean.upper()
                translation_dict[english_upper] = french_clean
                
                # Ajouter aussi une version avec guillemets au cas où le titre dans glossary les a
                translation_dict[f'"{english_upper}"'] = french_clean
    
    return translation_dict


def extract_chapters(glossary_file_path):
    """
    Extrait les chapitres du fichier input.
    Retourne une liste de tuples (titre_anglais, contenu).
    Préserver les retours à la ligne dans le contenu pour une meilleure lisibilité.
    """
    with open(glossary_file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    chapters = []
    current_chapter = None
    current_content = []
    
    for i, line in enumerate(lines):
        # Vérifier si c'est un titre de chapitre
        if is_chapter_title(line):
            # Vérifier que ce n'est pas au milieu d'un paragraphe
            # Un vrai titre devrait être précédé d'une ligne vide (ou être la première ligne)
            if i == 0 or not lines[i-1].strip():
                # Sauvegarder le chapitre précédent s'il existe
                if current_chapter is not None:
                    chapters.append((current_chapter, ''.join(current_content)))
                
                # Commencer un nouveau chapitre
                current_chapter = line.strip()
                current_content = [line]
                continue
        
        # Ajouter la ligne au contenu du chapitre actuel
        if current_chapter is not None:
            current_content.append(line)
    
    # Ajouter le dernier chapitre
    if current_chapter is not None:
        chapters.append((current_chapter, ''.join(current_content)))
    
    return chapters


def main():
    # Chemins des fichiers (à ajuster selon votre configuration)
    glossary_ref_file = '../.work/glossary_ref.txt'
    
    print("Parsing du fichier de référence...")
    translation_dict = parse_glossary_ref(glossary_ref_file)
    print(f"  {len(translation_dict)} traductions trouvées")
    
    print("\nExtraction des chapitres...")
    chapters = extract_chapters(input)
    print(f"  {len(chapters)} chapitres trouvés")
    
    print("\nGénération des fichiers .md...")
    stats = {
        'created': 0,
        'not_translated': 0,
        'errors': 0
    }
    
    not_translated = []
    
    for english_title, content in chapters:
        try:
            # Normaliser les guillemets dans le titre
            english_title_normalized = normalize_quotes(english_title)
            
            # Nettoyer le titre anglais pour la recherche
            english_upper = english_title_normalized.upper().strip()
            
            # Essayer de trouver la traduction avec et sans guillemets
            french_title = translation_dict.get(english_upper)
            
            # Si pas trouvé, essayer sans guillemets
            if not french_title:
                english_clean = english_upper.strip('"').strip()
                french_title = translation_dict.get(english_clean)

            if not french_title:
                french_title = english_clean # fallback

            if french_title:
                # Retrouver le fichier dans le dossier de sortie
                filename = clean_filename(french_title) + '.md'
                letter = french_title[0].upper()
                folder = os.path.join(output_dir, letter)
                filepath = os.path.join(folder, filename)

                # lire le fichier
                if os.path.exists(filepath):
                    with open(filepath, 'r', encoding='utf-8') as f:
                        existing_content = f.read()
                else:                    existing_content = ''

                content = existing_content.strip() + '\n\n\n'+version+'\n```\n' + content.strip() + '\n```'

                # Écrire le contenu dans le fichier
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content) 

                print(f"  ✓ {english_title} -> {filename}")
                stats['created'] += 1
            else:
                print(f"  ⚠ {english_title} -> {filename} (pas de traduction)")
                stats['not_translated'] += 1
                not_translated.append(english_title)
        
        except Exception as e:
            print(f"  ✗ Erreur pour {english_title}: {e}")
            stats['errors'] += 1
    
    # Afficher le résumé
    print("\n" + "="*60)
    print("RÉSUMÉ")
    print("="*60)
    print(f"Fichiers créés avec succès: {stats['created']}")
    print(f"Fichiers créés sans traduction: {stats['not_translated']}")
    print(f"Erreurs: {stats['errors']}")
    print(f"Total: {len(chapters)}")
    
    if not_translated:
        print(f"\nChapitres sans traduction ({len(not_translated)}):")
        for title in not_translated[:20]:  # Afficher les 20 premiers
            print(f"  - {title}")
        if len(not_translated) > 20:
            print(f"  ... et {len(not_translated) - 20} autres")
    
    print(f"\nFichiers générés dans le dossier: {output_dir}/")


if __name__ == '__main__':
    main()
