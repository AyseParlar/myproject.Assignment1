from collections import Counter
from operator import itemgetter

from django.conf import settings
from django.http import HttpResponse

# Create your views here.


def myview(request, filename):
    import os
    file_path = None
    for template_obj in settings.TEMPLATES:
        for template_path in template_obj['DIRS']:
            if os.path.exists(os.path.join(template_path, filename)):
                file_path = os.path.join(template_path, filename)
                break

    if file_path is None:
        from django.http.response import Http404
        raise Http404

    with open(file_path) as f:
        word_counts = Counter(f.read().replace('\n', ' ').replace('\r', '').split(' '))

    output = 'Name: {name}\nWords:'.format(name=filename)
    for word, count in sorted(word_counts.items(), key=itemgetter(1), reverse=True):
        output += '\n{w}, {c}'.format(w=word, c=count)

    return HttpResponse(output, content_type='text/plain')