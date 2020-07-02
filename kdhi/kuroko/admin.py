from django.contrib import admin
from django.contrib.auth.models import Group

from .models import face, figure, face_to_figure_link

admin.site.register(face)
admin.site.register(figure)
admin.site.register(face_to_figure_link)

