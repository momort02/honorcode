import os, sys

token   = os.environ.get('AIRTABLE_TOKEN', '')
base_id = os.environ.get('AIRTABLE_BASE_ID', '')

if not token or not base_id:
    print('ERREUR : secrets manquants', file=sys.stderr)
    sys.exit(1)

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('__AIRTABLE_TOKEN__',   token)
content = content.replace('__AIRTABLE_BASE_ID__', base_id)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

if '__AIRTABLE_TOKEN__' in content or '__AIRTABLE_BASE_ID__' in content:
    print('ERREUR : placeholders encore presents !', file=sys.stderr)
    sys.exit(1)

print('OK : secrets injectes avec succes.')