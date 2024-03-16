from django.contrib import admin
from .models import Publication

admin.site.site_header = " SemanaDev "
admin.site.index_title = " Semana Dev"

admin.site.register(Publication)






