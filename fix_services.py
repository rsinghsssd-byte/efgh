import os

files_to_fix = [
    'blogs/repositories/blog_repository.py',
    'blogs/services/image_service.py',
    'blogs/services/blog_service.py',
    'blogs/services/blog_regeneration_service.py'
]

for fpath in files_to_fix:
    with open(fpath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    out = []
    for line in lines:
        if 'user_id' in line:
            continue
        out.append(line)
        
    with open(fpath, 'w', encoding='utf-8') as f:
        f.writelines(out)

print("Done")
