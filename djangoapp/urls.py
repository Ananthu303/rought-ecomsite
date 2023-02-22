from django.urls import path
from .views import *
urlpatterns=[
    path('first/',first),
    path('audioupload/',audioupload),
    path('audiodisplay/',audiodisplay),
    path('shopreg/',shopreg),
    path('shoplog/',shoplog),
    path('productview/',productprofile),
    path('productupload/',productupload),
    path('productsdisplay/',productdisplay),
    path('allproductdisplay/',allproductdisplay),
    path('delete/<int:id>',productdelete),
    path('edit/<int:id>',productedit),
    path('ureg/',userreg),
    path('success/',success),
    path('verify/<auth_token>',verify),
    path('userlogin/',ulogin),
    path('userprofile/',userprofile),
    path('userallproducts/',userallproducts),
    path('index/',index),
    path('wishlist/<int:id>',wishlist),
    path('addtocart/<int:id>',addcart),
    path('cartdisplay/',displaycart),
    path('wishlistdisplay/',displaywishlist),
    path('removecart/<int:id>',removecart),
    path('wishremove/<int:id>',wishremove),
    path('cartbuy/<int:id>',cartbuy),
    path('wishtocart/<int:id>',wishlisttocart),
    path('placeorder/',cardpay),
    path('shopnot/',shopnotification),
    path('usernot/',usernotification)






]