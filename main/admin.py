from django.contrib import admin

from .models import Gallery
from .models import Listing

admin.site.register(Gallery)
admin.site.register(Listing)
