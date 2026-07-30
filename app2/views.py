from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'app2/index.html')
# Sign Up page
# name="name"
# name="mobile"
# name="email"
# name="dob"
# name="city"
# name="password"
# name="confirm_password"
# name="caccept"
def signup(request):
    if request.method=="POST":
        print("Request.method is running")
        user_name=request.POST.get('name')
        email=request.POST.get("email")
        mobile =request.POST.get("mobile")
        dateOfBirth=request.POST.get("dob")
        city=request.POST.get("city")
        password=request.POST.get("password")
        confirmPassword=request.POST.get("confirm_password")

        if password!=confirmPassword:
            messages.error(request, "Passwords do not match.")
            return redirect("signup")
        if Student.objects.filter(email=email).exists():
            messages.error(request,"This email is already exists!")
            return render('signup')
        if User.objects.filter(username=email).exists():
            messages.error(request,"User already exist!")
            return redirect("singnup")
        # create user for login
        user=User.objects.create_user(
            username=email,
            email=email,
            password=password
        )
        Student.objects.create(
            user_name=user_name,
            mobile=mobile,
            email=email,
            dateOfBirth=dateOfBirth,
            city=city,
            user_password=password
        )
        print("Registration successfully completed")
        messages.success(request, "Registration Successful.")
        return redirect("signin")
    return render(request,'app2/signup.html')
# Sign In page
def signIn(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=email,
            password=password
        )
        print("the value of user is : ",user)
        if user is not None:
            login(request, user)
            return redirect("dashboard")

        messages.error(request, "Invalid Email or Password.")

    return render(request, "app2/login.html")
# logout function 
def Logout(request):
    logout(request)
    return redirect("signin")
# dashboard function
@login_required(login_url='signin')
def dashboard(request):
    return render(request, "app2/dashboard.html")
 