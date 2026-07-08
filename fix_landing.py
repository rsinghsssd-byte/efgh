import re
import os

path = "templates/landing.html"
if os.path.exists(path):
    with open(path, "r") as f:
        text = f.read()

    text = text.replace("{% url 'login' %}", "{% url 'blogs:dashboard' %}")
    text = text.replace("{% url 'signup' %}", "{% url 'blogs:dashboard' %}")
    text = text.replace("Login", "Dashboard")
    text = text.replace("Get Started", "Open App")

    with open(path, "w") as f:
        f.write(text)
print("Updated landing.html")
