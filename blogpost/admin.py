from django.contrib import admin
from .models import BlogModel, SampleModel

# Register your models here.

admin.site.register(SampleModel)
admin.site.register(BlogModel)