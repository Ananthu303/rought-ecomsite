from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(shopregmodel)
admin.site.register(productuploadmodel)
admin.site.register(profile)
admin.site.register(cart)
admin.site.register(wishlistm)
admin.site.register(buy)
admin.site.register(customerdetailsmodel)
