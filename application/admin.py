from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(News_Model)
admin.site.register(source_name)
admin.site.register(source_select)



admin.site.site_header = "News Aggregator"