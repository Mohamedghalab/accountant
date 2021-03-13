from django.contrib import admin
from .models import *

admin.site.register(Company)
admin.site.register(Importer)
admin.site.register(Category)
admin.site.register(Price)
admin.site.register(Customer)
admin.site.register(Invoice)

