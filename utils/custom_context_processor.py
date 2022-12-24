from .constants import TAGS

# https://stackoverflow.com/questions/60271748/how-to-pass-a-variable-from-views-to-base-html-in-django
# https://betterprogramming.pub/django-quick-tips-context-processors-da74f887f1fc
def tag_renderer(request):
    return {
       'tags': dict(TAGS),
    }
