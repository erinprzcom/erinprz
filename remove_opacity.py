import os
import re

files_to_check = ['index.html', 'sketches.html', 'book.html', 'build_mock.py']

for filepath in files_to_check:
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            content = f.read()

        # We want to remove the overlay div completely
        # It could be single line or split across lines
        pattern = r'<div class="absolute inset-0 bg-black bg-opacity-0 group-hover:bg-opacity-20 transition-opacity duration-300">\s*</div>\n?'
        
        new_content, count = re.subn(pattern, '', content)
        
        # also check for without newlines or different spaces just in case
        if count > 0:
            with open(filepath, 'w') as f:
                f.write(new_content)
            print(f"Updated {filepath}: removed {count} overlays")
        else:
            print(f"No changes in {filepath}")

