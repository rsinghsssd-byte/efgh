import os

for root, _, files in os.walk('templates'):
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()

            content = content.replace('blog.status=="draft"', 'blog.status == "draft"')
            content = content.replace('blog.status=="published"', 'blog.status == "published"')
            content = content.replace('blog.status=="archived"', 'blog.status == "archived"')

            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)

print("Fixed template tags")
