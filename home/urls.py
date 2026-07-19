from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
    path("", views.home_page, name="home"),

    path(
        "information-centre/",
        views.information_centre,
        name="information-centre",
    ),

    path(
        "information-centre/password-security/",
        views.password_security,
        name="password-security",
    ),
]
urlpatterns = [
    # ... your existing paths (like index or information_centre) ...
    path('read-more-1/', views.readmore1, name='readmore1_page'),
]