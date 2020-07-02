
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
	face_isnt_name = face_inst.image_filename
	face_isnt_name = face_isnt_name.split(".")[0]
	try:
		kdhi_linked_individual = individual.objects.get(name=face_isnt_name)
		figure_inst = figure(
			name=face_isnt_name, 
			kdhi_db_figure=kdhi_linked_individual,
			)
		figure_inst.save()
	except:
		figure_inst = figure(
			name=face_isnt_name, 
			)
		figure_inst.save()
		print("No object for {} in bios!".format(face_isnt_name))

