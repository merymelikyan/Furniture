from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name= "index"),
    path("about/", views.about, name= "about"),
    path("furniture/", views.furniture, name= "furniture"),
    path("blog/", views.blog, name= "blog"),
    path("contact/", views.contact, name= "contact"),
    path("blog/<int:blog_id>/", views.single_blog, name= "blog"),
]
