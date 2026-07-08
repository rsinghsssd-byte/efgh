import re
import os

def process_dashboard_views():
    path = "dashboard/views.py"
    if not os.path.exists(path): return
    with open(path, "r") as f:
        text = f.read()
    
    text = text.replace("from core.decorators import login_required\n", "")
    text = text.replace("@login_required\n", "")
    text = re.sub(r'\s*"email": request\.email,', '', text)
    text = re.sub(r'\s*"user_id": request\.user_id,', '', text)
    
    with open(path, "w") as f:
        f.write(text)

def process_blogs_views():
    path = "blogs/views.py"
    if not os.path.exists(path): return
    with open(path, "r") as f:
        text = f.read()

    text = text.replace("from core.decorators import login_required\n", "")
    text = text.replace("@method_decorator(login_required, name=\"dispatch\")\n", "")
    text = text.replace("@login_required\n", "")
    
    # GenerateBlogView
    text = re.sub(r'\s*if "user" not in request\.session:\s*return redirect\("login"\)', '', text)
    text = re.sub(r'\s*user_id=request\.session\["user"\]\["id"\],', '', text)
    
    # DashboardView
    text = re.sub(r'\s*user = request\.session\.get\("user"\)\s*if not user:\s*return redirect\("login"\)\s*user_id = user\["id"\]', '', text)
    text = re.sub(r'\s*user_id=user_id,', '', text)
    
    # my_blogs
    text = re.sub(r'\s*request\.user\["id"\],', '', text)
    text = re.sub(r'\s*user_id=request\.user\["id"\],', '', text)
    
    # edit_blog
    text = re.sub(r'\s*if str\(blog\.user_id\) != request\.user\["id"\]:\s*return redirect\("blogs:my_blogs"\)', '', text)
    
    # JSON responses
    auth_check_block = (
        r'\s*if str\(blog\.user_id\) != request\.user\["id"\]:'
        r'\s*return JsonResponse\('
        r'\s*\{\s*"success":\s*False,\s*"message":\s*"Permission denied\.?"\s*\},'
        r'\s*status=403,\s*\)'
    )
    text = re.sub(auth_check_block, '', text)
    
    text = re.sub(
        r'\s*if str\(blog\.user_id\) != request\.user\["id"\]:\s*return JsonResponse\(\s*\{\s*"success":False,\s*"message":"Permission denied"\s*\},\s*status=403,\s*\)',
        '', text
    )
    
    # regenerate_image
    text = re.sub(r'\s*user_id=request\.user\["id"\],', '', text)
    
    with open(path, "w") as f:
        f.write(text)

def process_services():
    # blog_service.py
    p = 'blogs/services/blog_service.py'
    if os.path.exists(p):
        with open(p, 'r') as f: t = f.read()
        t = re.sub(r'user_id=user_id,', '', t)
        t = re.sub(r'def generate\(self,\s*request: BlogRequest,\s*user_id: str,\s*\)', r'def generate(self, request: BlogRequest)', t)
        with open(p, 'w') as f: f.write(t)

    # image_service.py
    p = 'blogs/services/image_service.py'
    if os.path.exists(p):
        with open(p, 'r') as f: t = f.read()
        # image_service: def generate_and_store_image(cls, prompt: str, image_name: str, blog: Blog, user_id: str) -> StoredImage
        t = re.sub(r'user_id:\s*str,?\s*', '', t)
        t = re.sub(r'user_id=user_id,', '', t)
        with open(p, 'w') as f: f.write(t)
        
    # storage_service.py
    p = 'blogs/services/storage_service.py'
    if os.path.exists(p):
        with open(p, 'r') as f: t = f.read()
        t = re.sub(r'user_id:\s*str,?\s*', '', t)
        t = t.replace('f"users/{user_id}/', 'f"public/')
        t = t.replace('users/{user_id}/', 'public/')
        with open(p, 'w') as f: f.write(t)

    # regenerate_service.py
    p = 'blogs/services/regenerate_service.py'
    if os.path.exists(p):
        with open(p, 'r') as f: t = f.read()
        t = re.sub(r'user_id:\s*str,?\s*', '', t)
        t = re.sub(r'user_id=user_id,', '', t)
        with open(p, 'w') as f: f.write(t)
        
    # blog_repository.py
    p = 'blogs/repositories/blog_repository.py'
    if os.path.exists(p):
        with open(p, 'r') as f: t = f.read()
        t = re.sub(r'user_id:\s*str,?\s*', '', t)
        t = re.sub(r'user_id=user_id,?\s*', '', t)
        with open(p, 'w') as f: f.write(t)
        
process_dashboard_views()
process_blogs_views()
process_services()
print("Done processing.")
