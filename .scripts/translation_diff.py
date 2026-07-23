import argparse
import glob
import os
import re
import difflib

DETAILS_RE = re.compile(r'<details class="source">\s*<summary>(.*?)</summary>(.*?)</details>', re.S)


def extract_section(text, label):
    for m in DETAILS_RE.finditer(text):
        if m.group(1).strip() == label:
            return m.group(2).strip()
    return None


def file_diff(path):
    text = open(path, encoding='utf-8').read()
    v18 = extract_section(text, 'EN v1.8')
    v17 = extract_section(text, 'EN v1.7')
    fr = extract_section(text, 'FR v1.4')
    return v17, v18, fr


def print_diff(path, v17, v18):
    print(f'=== {os.path.basename(path)} ===')
    if v17 is None or v18 is None:
        print('Missing EN v1.7 or EN v1.8 block')
        return
    if v17 == v18:
        print('No diff between EN v1.7 and EN v1.8')
        return
    for line in difflib.unified_diff(v17.splitlines(), v18.splitlines(), lineterm=''):
        print(line)


def count_bullets(text):
    if text is None:
        return 0
    return text.count('•') + text.count('» »')


def main():
    parser = argparse.ArgumentParser(description='Compare EN v1.8 and EN v1.7 sections in glossary files.')
    parser.add_argument('folder', nargs='?', default='docs/Glossaire/C', help='Folder to scan')
    parser.add_argument('--diff', action='store_true', help='Show unified diff for changed files')
    args = parser.parse_args()

    folder = os.path.abspath(args.folder)
    files = sorted(glob.glob(os.path.join(folder, '*.md')))
    changed = []
    for path in files:
        v17, v18, fr = file_diff(path)
        if v17 is None or v18 is None:
            continue
        if v18 != v17:
            changed.append((path, v17, v18, fr))

    print(f'Found {len(changed)} changed files in {folder}')
    for path, v17, v18, fr in changed:
        print(os.path.basename(path))
        if args.diff:
            print_diff(path, v17, v18)
            print()

    if not args.diff and changed:
        print('\nRun with --diff to see the exact changes.')


if __name__ == '__main__':
    main()
