import json
import shutil
import os
from pathlib import Path

print('Reading files.json...')
try:
    with open('files.json', 'r') as f:
        content = f.read()
        print(f'Raw content: {repr(content)}')
        files = json.loads(content)
except Exception as e:
    print(f'Error reading files.json: {e}')
    import traceback
    traceback.print_exc()
    exit(1)

print(f'Files to copy: {files}')

for file_path in files:
    source = Path('staging') / file_path
    dest = Path(file_path)
    
    print(f'Checking source: {source}')
    print(f'Source exists: {source.exists()}')
    
    if source.exists():
        # Ensure destination directory exists
        dest.parent.mkdir(parents=True, exist_ok=True)
        
        # Copy file
        shutil.copy2(source, dest)
        print(f'Successfully copied: {source} -> {dest}')
    else:
        print(f'ERROR: Source file not found: {source}')
        # List what's actually in the staging directory
        files_dir = Path('staging')
        if files_dir.exists():
            print(f'Contents of staging: {list(files_dir.rglob("*"))}')
        else:
            print('staging directory does not exist!')
