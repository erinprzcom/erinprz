import re

with open('book.md', 'r') as f:
    content = f.read()

# Replace frontmatter and add includes
content = re.sub(
    r'^---\nlayout: page\n---\n',
    '---\n---\n\n{% include head.html %}\n{% include header.html %}\n',
    content,
    flags=re.MULTILINE
)

# Change container to max-w-8xl
content = content.replace(
    '<div class="not-prose max-w-5xl mx-auto my-12">',
    '<main class="max-w-8xl mx-auto px-4 sm:px-6 lg:px-8 py-12">'
)

# Replace the closing div with closing main and add footer includes
content = content.replace(
    '  </div>\n</div>',
    '  </div>\n</main>\n\n{% include footer.html %}\n{% include googleanalytics.html %}\n</body>\n</html>'
)

# Update the CSS for 3 columns
old_css = '''  @media (min-width: 1024px) {
    .masonry-item {
      width: calc(50% - 16px);
    }
  }'''

new_css = '''  @media (min-width: 1024px) {
    .masonry-item {
      width: calc(33.333% - 22px);
    }
  }'''

content = content.replace(old_css, new_css)

with open('book.md', 'w') as f:
    f.write(content)

