
from django.urls import path

from . import views # . means the current directory

urlpatterns = [
    path("", views.index, name="index"), # "" means the root path of the application (i.e. http:// localhost:8000/) and
    # views.index means the index function in the views.py file of the hello application 
]