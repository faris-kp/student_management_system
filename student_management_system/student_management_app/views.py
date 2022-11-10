from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login,logout
from django.http import HttpResponseRedirect
from student_management_app.EmailBackEnd import EmailBackEnd



# Create your views here.



def ShowDemo(request):
    return render(request,"demo.html")

def ShowLoginPage(request):
    return render(request,"login_page.html")


def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method not Allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            print("user_cheking",user.user_type)
            if user.user_type =="1":
                return redirect("admin_home")         
            elif user.user_type =="2":
                return redirect("staff_home")
            else:
                return redirect("student_home")
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")

def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("user:"+request.user.email+"user_type:"+request.user.user_type)
    
def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")
