from .utils import TAGS

print(dict(TAGS))


def tag_renderer(request):
    return {
       'tags': dict(TAGS),
    }
