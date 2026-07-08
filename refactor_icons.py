import os

target = 'templates/blogs/edit_blog.html'

with open(target, 'r', encoding='utf-8') as f:
    html = f.read()

# Emojis to replace
# 💾
save_icon = '<i data-lucide="save" class="w-5 h-5 inline-block -mt-1 mr-1"></i> '
html = html.replace('💾 ', save_icon)
html = html.replace('💾', save_icon)

# 🖼
image_icon = '<i data-lucide="image" class="w-5 h-5 inline-block -mt-1 mr-1"></i> '
html = html.replace('🖼 ', image_icon)
html = html.replace('🖼', image_icon)

# ✨
sparkle_icon = '<i data-lucide="sparkles" class="w-5 h-5 inline-block -mt-1 mr-1"></i> '
html = html.replace('✨ ', sparkle_icon)
html = html.replace('✨', sparkle_icon)

with open(target, 'w', encoding='utf-8') as f:
    f.write(html)

print("Icons updated")
