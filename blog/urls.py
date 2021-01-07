from django.urls import path
from . import views

app_name='Blog'

urlpatterns=[
    path("", views.index, name="index"),
    path("<int:blog_id>", views.detail, name="detail")
]