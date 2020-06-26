import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kdhi.settings")
from django.conf import settings
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from trackers.models import inter_korean_tracker, inter_korean_category, inter_korean_subcategory, inter_korean_level
from main_site.models import rok_individual, individual
import csv
import string

event_deleted = inter_korean_tracker.objects.get(MOU_description='').update(event_itteration='')