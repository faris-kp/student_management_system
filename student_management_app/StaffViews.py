from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from student_management_app.models import Subjects,SessionYearModel,Students

def staff_home(request):
    return render(request,"staff_template/staff_home_template.html")

def staff_take_attendence(request):
    subjects = Subjects.objects.filter(staff_id = request.user.id)
    session_years = SessionYearModel.objects.all()
    return render(request,"staff_template/staff_take_attendence.html",{"subjects":subjects,"session_years":session_years})

@csrf_exempt
def get_students(request):
    print("Entering into funtion")
    subject_id = request.POST.get('subject',False)
    print("..",subject_id)
    session_year = request.POST.get('session_year',False)
    print(",,,",session_year)
    subject = Subjects.objects.get(id=subject_id)
    print("get student",subject)
    session_model = SessionYearModel.objects.get(id=session_year)
    print("sesseion chekc",session_model)

    students=Students.objects.filter(course_id=subject.course_id,session_year_id=session_model)
    print("studets chechk",students)
    return HttpResponse(students)

