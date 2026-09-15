from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("about/",views.about, name="about"),
    path('add-article/', views.add_article, name='add_article'),
    path(
        "newsletter/subscribe/",
        views.newsletter_subscribe,
        name="newsletter_subscribe"
    ),
    path("faq/", views.faq, name="faq"),
    path("privacy/", views.privacy, name="privacy"),
    path("terms/", views.terms, name="terms"),
]