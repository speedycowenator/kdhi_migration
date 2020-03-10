

import os
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kdhi.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from news_archive.models import article_model



pk=11
test_object = article_model.objects.get(pk=pk)


full_text = test_object.summary
search_term = 'Juche'
full_text = test_object.summary

full_text_sentences = full_text.split('. ')

html_tag_front = '''<span class="search_highlight">'''
html_tag_back = "</span>"
marked_search_text = '...'

for line in full_text_sentences:
    match = re.search(search_term, line)
    if match:
        line_highlights = line
        highlighted_search_term = html_tag_front + search_term + html_tag_back
        line_highlights = re.sub(search_term, highlighted_search_term, line_highlights)
        marked_search_text += line_highlights + '...'
print(marked_search_text)