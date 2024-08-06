
from django.urls import path
from .import views 

urlpatterns = [
    path("index", views.indexpage, name="indexpage"),
    path("about", views.aboutpage, name="aboutpage"),
    path("service", views.servicepage, name="servicepage"),
    path("contact", views.contactpage, name="contactpage"),
    path("signin", views.signin, name="signinpage"),
    path("signup", views.signup.as_view(), name="signuppage"),
    path("stuadmin", views.stuadmin.as_view(), name="stuadmin"),
    path("stunotess", views.stunotess.as_view(), name="stunotess"),
    path("stunoteupdate/<int:id>", views.stunoteupdate.as_view(), name="stunoteupdate"),
    path("stuhomeworks", views.stuhomeworks.as_view(), name="stuhomeworks"),
    path("stulistview", views.stulistview.as_view(), name="stulistview"),
    path("teacherslist", views.teacherslist.as_view(), name="teacherslist"),

    path("teaadmin", views.teaadmin.as_view(), name="teaadmin"),
    path("teaclass06", views.teaclass06.as_view(), name="teaclass06"),
]

