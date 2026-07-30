from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import registration as regs ,testtable
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def index(request):
    # return HttpResponse("<h1>This is sindex file</h1>")
    return render(request,'user/index.html')

#admin login 
def adminlogin(request):
    return render(request,"app2/index.html")
def test1(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get("lname")
        mom=request.POST.get("mom")
        father=request.POST.get("father")
        address=request.POST.get("address")
        gender=request.POST.get("gender")
        state=request.POST.get("state")
        city=request.POST.get("city")
        dob=request.POST.get("dob")
        course=request.POST.get("course")
        pincode=request.POST.get("pincode")
        email=request.POST.get("email")
        t=testtable()
        t.firstName=fname
        t.lastName=lname
        t.motherName=mom
        t.fatherName=father
        t.address=address
        t.gender=gender
        t.state=state
        t.city=city
        t.DateOfBirth=dob
        t.pincode=pincode
        t.course=course
        t.email=email
        t.save()
        return redirect('index')
    # """
    # fname=Devanand
    # lname=Rai
    # mom=basanti
    # father=ramgrah
    # address=TIWARI+TOLA%2CBARI+GAV%2CGHUGHULI+BUZURG%2CMAHARAJGANJ
    # gender=male
    # state=Uttar+Pradesh
    # city=maharajganj
    # dob=2026-07-01
    # pincode=273151
    # course=btech
    # email=devanandrai3260%40gmail.com
    # """
    return render(request,"user/test1.html")


def test2(request):
    return render(request,"user/test2.html")


def test3(request):
    return render(request,"user/test3.html")


def registration(request):
    if request.method=="POST":
        name=request.POST.get('name')
        Email=request.POST.get("Email")
        pwd=request.POST.get("pwd")
        chpwd=request.POST.get("chpwd")
        tick=bool(request.POST.get("tick"))
        if pwd!=chpwd:
            return render(request,'user/registration.html',{"color":"warning","regmsg":"Password didn't match!"})
        if User.objects.filter(username=name).exists():
            return render(request,'user/registration.html',{"color":'danger','regmsg':"Name is already exist!"})
        if User.objects.filter(email=Email).exists():
            return render(request,'user/registration.html',{"color":"primary",'regmsg':"This email is already in user"})
        # Save the data in the registration model 
        reg=regs()
        reg.name=name
        reg.Email=Email
        reg.password=pwd
        reg.dateTime=datetime
        reg.save()
        #Create user
        user=User.objects.create_user(
            email=Email,
            username=name,
            password=pwd,

        )
        #login automatically
        login(request,user)
        return redirect("dashboard")
    return render(request,'user/registration.html')






# from django.contrib.auth import authenticate, login

def userlogin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user= User.objects.get(Email=email)
        except User.DoesNotExist:
            print("user Doesn't exist")
            return render(request, "user/login.html", {
                "error": "Invalid Email"
            })

        user = authenticate(
            request,
            username=email,
            password=password
        )
        print("user: ==============================",user)
        if user is not None:
            login(request, user)
            return redirect("dashboard")

        return render(request, "user/login.html", {
            "error": "Invalid Password"
        })

    return render(request, "user/login.html")


def userlogout(request):
    logout(request)
    return redirect("login")   # Redirect to login page

def dashboard(request):
    return render(request,'user/dashboard.html')

























































































































# def registration(request):
#     """
#     name=DEVANAND+RAI
#     Email=DEVANANDRAI3260%40GMAIL.COM
#     pwd=123
#     chpwd=1234
#     tick=TRUE
#     """
  
#     regmsg=''
#     color=''
#     if request.method=="POST":
#         name=request.POST.get('name')
#         Email=request.POST.get("Email")
#         pwd=request.POST.get("pwd")
#         chpwd=request.POST.get("chpwd")
#         tick=bool(request.POST.get("tick"))
        
#         if tick and chpwd==pwd:
#             regmsg="Registration complete successfully!"
#             color='success'
#             reg=regs()
#             reg.name=name
#             reg.Email=Email
#             reg.password=pwd
#             reg.dateTime=datetime
#             reg.save()
#             return redirect('registration')
#         elif not tick and chpwd==pwd:
#             regmsg="Please accept the conditon"
#             color="danger"
#         elif chpwd!=pwd and tick:
#             regmsg="Password didn't match"
#             color='danger'
#         else:
#             regmsg="There is something wrong!"
#             color='warning'

#     return render(request,"user/registration.html",context={'regmsg':regmsg,"color":color})
if __name__=="__main__":
    registration()