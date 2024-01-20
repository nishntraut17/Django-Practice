# myproject/urls.py
from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("success-page/", success_page, name="success-page"),
    path("contact/", contact, name="contact"),
    path("about/", about, name="about"),
]
