from django.urls import path
from django.urls.resolvers import URLPattern
from .views import contact


app_name = "contact"

urlpatterns = [

    path("", contact, name="contact")


]