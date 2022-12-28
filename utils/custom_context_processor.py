from .constants import TAGS


def tag_renderer(request):
    """
    Makes tuple of tags available in all templates

    Tutorials available at
    https://stackoverflow.com/questions/60271748/how-to-pass-a-variable-from-views-to-base-html-in-django
    https://betterprogramming.pub/django-quick-tips-context-processors-da74f887f1fc
    """
    return {
       'tags': dict(TAGS),
    }
