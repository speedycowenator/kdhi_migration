

import os
import re


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kdhi.setting")
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from kdhi.models import article
application = get_wsgi_application()

pk = 75000
test_object = article.objects.get(pk=pk)

seed = ['publication', 'dedicates', 'fifth anniversary']

pattern = re.compile(r'\b(?:' + '|'.join(re.escape(s) for s in seed) + r')\b')


full_text = '''Rodong Sinmun Wednesday dedicates an article to the fifth anniversary of the publication of Supreme Leader ''Kim Jong Un's work "Let the Entire Party, the Whole Army and All the People Conduct a Vigorous Forest Restoration Campaign to Cover the Mountains of the Country with Green Woods. "The work indicates detailed tasks to restore forest including the issues of simultaneously pushing forward with tree-planting movement and forest conservation and of developing.'''

full_text_sentences = full_text.split('. ')

html_tag_front = '''<span class="search_highlight">'''
html_tag_back = "</span>"


for line in full_text_sentences:
    line_highlights = line
    line_score = len(pattern.findall(line))
    for search_term in seed:
        highlighted_search_term = html_tag_front + search_term + html_tag_back
        line_highlights = re.sub(search_term, highlighted_search_term, line_highlights)
    print(line_highlights)
        
        