from django.urls import path
from user import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/adminlogin",views.adminlogin,name="adminlogin"),
    path("/test1", views.test1, name="test1"),
    path("/test2", views.test2, name="test2"),
    path("/test3", views.test3, name="test3"),
    path("/registration", views.registration, name="registration"),
    path("/userlogin", views.userlogin, name="login"),
    path("/logout", views.userlogout, name="logout"),
    path("/dashboard", views.dashboard, name="dashboard"),
]