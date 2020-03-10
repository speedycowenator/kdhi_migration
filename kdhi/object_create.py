

import os
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kdhi.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from main_site.models import individual, institution, position

ind     = individual.objects.get(pk=1)
ins     = institution.objects.get(pk=1)
pos     = position(
            person              = ind,
            institution         = ins,
            title               = 'Chairman',
        )

pos.save()