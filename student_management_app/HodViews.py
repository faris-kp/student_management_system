from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponseRedirect
from student_management_app.models import Courses, CustomUser, Staffs, Students, Subjects,SessionYearModel
from django.core.files.storage import FileSystemStorage
from .forms import AddStudentForm,EditStudentForm

def admin_home(request):
    return render(request,"hod_template/home_content.html")

def add_staff(request):
    return render(request, "hod_template/add_staff_template.html")

def add_staff_save(request):
    if request.method!="POST":
        print("get")
        return HttpResponse("Method not allowed")
    else:
        print("Enter into Staff POST")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        try:
            user = CustomUser.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name,user_type=2)
            user.staffs.address = address
            user.save()
            messages.success(request,"Successuly added staff")
            return redirect("add_staff")
        except:
            print("error")
            messages.error(request,"Failed to add staff")
            return redirect("add_staff")


def manage_staff(request):
    staffs = Staffs.objects.all()
    return render(request,"hod_template/manage_staff_template.html",{"staffs":staffs})

def edit_staff(request,staff_id):
    staff = Staffs.objects.get(admin=staff_id)
    return render(request,"hod_template/edit_staff_template.html",{"staff":staff,"id":staff_id})

def edit_staff_save(request):
    if request.method !="POST":
        return HttpResponse("Method not allowed")
    else:
        staff_id=request.POST.get("staff_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        address = request.POST.get("address")
        try:
            user = CustomUser.objects.get(id=staff_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.save()
            staff_model = Staffs.objects.get(admin=staff_id)
            staff_model.address=address
            staff_model.save()
            messages.success(request,"Successuly edit staff")
            return HttpResponseRedirect(reverse("edit_staff",kwargs={"staff_id":staff_id}))
        except:
            messages.error(request,"Failed to  add staff")
            return HttpResponseRedirect(reverse("edit_staff",kwargs={"staff_id":staff_id}))



def add_course(request):
    return render(request,"hod_template/add_course_template.html")

def add_course_save(request):
    if request.method!="POST":
        return HttpResponse("method not allowed")
    else:
        course = request.POST.get("course")
        try:
            course_model = Courses(course_name=course)
            course_model.save()
            messages.success(request,"Successuly added course")
            return redirect("add_course")
        except:
            print("error")
            messages.error(request,"Failed to add course")
            return redirect("add_course")

def manage_courses(request):
    courses = Courses.objects.all()
    return render(request,"hod_template/manage_course_template.html",{"courses":courses})
            
def edit_course(request,course_id):
    course = Courses.objects.get(id=course_id)
    return render(request,"hod_template/edit_course_template.html",{"course":course,"id":course_id})

def edit_course_save(request):
    if request.method!="POST":
        return HttpResponse("method not allowed")
    else:
        course_id = request.POST.get('course_id')
        course_name = request.POST.get('course')
    try:
        course = Courses.objects.get(id=course_id)
        course.course_name=course_name
        course.save()
        messages.success(request,"Successuly edit course")
        return HttpResponseRedirect(reverse("edit_course",kwargs={"course_id":course_id}))
    except:
        messages.error(request,"Failed  to  edit course")
        return HttpResponseRedirect(reverse("edit_course",kwargs={"course_id":course_id}))


def add_subject(request):
    courses = Courses.objects.all()
    staffs = CustomUser.objects.filter(user_type=2)
    context = {
        'courses':courses,
        'staffs':staffs
    }
    return render(request,"hod_template/add_subject_template.html",context)

def add_subject_save(request):
    if request.method!="POST":
        return HttpResponse("method not allowed")
    else:
        subject_name = request.POST.get("subject_name")
        course_id = request.POST.get("course")
        course = Courses.objects.get(id=course_id)
        staff_id = request.POST.get("staff")
        staff =  CustomUser.objects.get(id=staff_id)
        try:
            subject = Subjects(subject_name=subject_name,course_id=course,staff_id=staff)
            subject.save()
            messages.success(request,"Successuly added subject")
            return redirect("add_subject")
        except:
            print("error")
            messages.error(request,"Failed to add subject")
            return redirect("add_subject")

def edit_subject(request,subject_id):
    subject = Subjects.objects.get(id=subject_id)
    course = Courses.objects.all()
    staff = CustomUser.objects.filter(user_type=2)
    return render(request,"hod_template/edit_subject_template.html",{ "subject":subject,"courses":course,"staffs":staff ,"id":subject_id})

def edit_subject_save(request):
    if request.method!="POST":
        return HttpResponse("method not allowed")
    else:
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject_name')
        staff_id = request.POST.get('staff')
        course_id = request.POST.get('course')
    try:
        subject = Subjects.objects.get(id=subject_id)
        subject.subject_name=subject_name
        course=Courses.objects.get(id=course_id)
        staff=CustomUser.objects.get(id=staff_id)
        subject.course_id = course
        subject.staff_id = staff
        subject.save()
        messages.success(request,"Successuly edit subject")
        return HttpResponseRedirect(reverse("edit_subject",kwargs={"subject_id":subject_id}))
    except:
        messages.error(request,"Failed  to  edit subject")
        return HttpResponseRedirect(reverse("edit_subject",kwargs={"subject_id":subject_id}))

def manage_subjects(request):
    subjects = Subjects.objects.all()
    return render(request,"hod_template/manage_subject_template.html",{"subjects":subjects})
            



def add_student(request):
    form = AddStudentForm()
    return render(request, "hod_template/add_student_template.html",{"form":form})


def add_student_save(request):
    if request.method!="POST":
        return HttpResponse("method not allowed")
    else:
        form=AddStudentForm(request.POST,request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            address = form.cleaned_data["address"]
            session_year_id = form.cleaned_data["session_year_id"]
            course_id = form.cleaned_data["course"]
            sex = form.cleaned_data["sex"]
            profile_pic = form.cleaned_data["profile_pic"]
            fs=FileSystemStorage()
            filename=fs.save(profile_pic.name,profile_pic)
            profile_pic_url = fs.url(filename)
            try:
                 user = CustomUser.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name,user_type=3)
                 user.students.address = address
                 course_obj = Courses.objects.get(id=course_id)
                 user.students.course_id = course_obj
                 session_year = SessionYearModel.objects.get(id=session_year_id)
                 user.students.session_year_id = session_year
                 user.students.gender=sex
                 user.students.profile_pic=profile_pic_url
                 user.save()
                 messages.success(request,"Successuly added students")
                 return redirect('add_student')
            except:
                messages.error(request,"Failed to  added students")
                return redirect('add_student')
        else:
            form=AddStudentForm(request.POST)
            return render(request, "hod_template/add_student_template.html",{"form":form})


def manage_student(request):
    students = Students.objects.all()
    return render(request,"hod_template/manage_student_template.html",{"students":students})


def edit_student(request,student_id):
    request.session['student_id']=student_id
    student = Students.objects.get(admin=student_id)
    form = EditStudentForm()
    form.fields['email'].initial=student.admin.email
    form.fields['first_name'].initial=student.admin.first_name
    form.fields['last_name'].initial=student.admin.last_name
    form.fields['username'].initial=student.admin.username
    form.fields['address'].initial=student.address
    form.fields['course'].initial=student.course_id.id
    form.fields['sex'].initial=student.gender
    form.fields['session_year_id'].initial=student.session_year_id.id
    
    return render(request,"hod_template/edit_student_template.html",{"form":form,"id":student_id,"username":student.admin.username})

def edit_student_save(request):
    if request.method !="POST":
        return HttpResponse("Method not allowed")
    else:
        student_id = request.session.get("student_id")
        if student_id==None:
            return redirect("manage_student")
        form=EditStudentForm(request.POST,request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            address = form.cleaned_data["address"]
            session_year_id = form.cleaned_data["session_year_id"]
            course_id = form.cleaned_data["course"]
            sex = form.cleaned_data["sex"]
            if request.FILES.get('profile_pic',False):
                profile_pic=request.FILES['profile_pic']
                print("profile pic cheking",profile_pic)
                fs=FileSystemStorage()
                filename=fs.save(profile_pic.name,profile_pic)
                profile_pic_url=fs.url(filename)
            else:
                profile_pic_url=None
            try:
                user = CustomUser.objects.get(id=student_id)
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.username = username
                user.save()
                student = Students.objects.get(admin=student_id)
                student.address=address
                session_year = SessionYearModel.objects.get(id=session_year_id)
                student.session_year_id = session_year
                student.gender = sex
                if profile_pic_url != None:
                    student.profile_pic = profile_pic_url
                course = Courses.objects.get(id=course_id) 
                student.course_id = course
                student.save()
                del request.session['student_id']
                messages.success(request,"Successuly edit student")
                return HttpResponseRedirect(reverse("edit_student",kwargs={"student_id":student_id}))
            except:
                messages.error(request,"Failed to  add student")
                return HttpResponseRedirect(reverse("edit_student",kwargs={"student_id":student_id}))
        else:
            form=EditStudentForm(request.POST)
            student = Students.objects.get(admin=student_id)
            return render(request,"hod_template/edit_student_template.html",{"form":form,"id":student_id,"username":student.admin.username})

def manage_session(request):
    return render(request,"hod_template/manage_session_template.html")


def add_session_save(request):
    if request.method!="POST":
        return redirect('manage_session')
    else:
        session_start_year = request.POST.get("session_start")
        session_end_year = request.POST.get("session_end")
        try:
            sessionyear=SessionYearModel(session_start_year=session_start_year,session_end_year=session_end_year)
            sessionyear.save()
            messages.success(request,"Successuly Add Session")
            return HttpResponseRedirect(reverse("manage_session"))
        except:
            messages.error(request,"Failed to  Add Session")
            return HttpResponseRedirect(reverse("manage_session"))