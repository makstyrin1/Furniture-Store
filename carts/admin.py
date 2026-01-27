from django.contrib import admin
from django.views.debug import default_urlconf

from carts.models import Cart



admin.site.register(Cart)
