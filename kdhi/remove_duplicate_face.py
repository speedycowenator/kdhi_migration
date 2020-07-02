
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

face_objects = face.objects.all()
for face_inst in face_objects:
	face_isnt_name = face_inst.name
	try:
		duplicate = face.objects.get(name=face_isnt_name)
	except:
		print("Found duplicate for {}".format(face_isnt_name))
		face_inst.delete()
		print("Deleted {}".format(face_isnt_name))
