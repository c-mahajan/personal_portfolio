from django.urls import path
from . import views

app_name="Portfolio"

urlpatterns=[
    path("", views.index, name='index')
]