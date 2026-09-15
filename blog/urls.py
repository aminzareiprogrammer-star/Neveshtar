from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
   path("",views.blog, name="blog"),
   path("article/<str:slug>",views.article, name="article"),
   path("category/<int:pk>/", views.category, name="category"),
   path("search/", views.search, name="search"),
   path("contact/", views.contact, name="contact"),
    path(
        "like/<int:id>/",
        views.like_view,
        name="like"
    ),
path(
    "comment/<int:comment_id>/like/",
    views.like_comment,
    name="like_comment"),

]