
from datetime import date, timedelta
import bs4
import urllib.request
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kdhi.settings")
from django.conf import settings
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from main_site.models import institution, individual, position, rok_individual
from kuroko.models import face, figure

face_objects = face.objects.filter(verified_figure__isnull=True)
for face_inst in face_objects:
	face_isnt_name = face_inst.image_filename
	face_isnt_name = face_isnt_name.split(".")[0]
	try:
		linked_figure = figure.objects.get(name=face_isnt_name)
		face_inst.verified_figure = linked_figure
		face_inst.save()
	except:
		print(face_inst)
