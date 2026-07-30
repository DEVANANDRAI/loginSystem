from django.urls import path
from app2 import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup",views.signup,name="signup"),
    path("signin",views.signIn,name="signin"),
    path("logout",views.Logout,name="logout"),

]