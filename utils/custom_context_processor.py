from .utils import TAGS

# https://betterprogramming.pub/django-quick-tips-context-processors-da74f887f1fc
def tag_renderer(request):
    return {
       'tags': dict(TAGS),
    }
