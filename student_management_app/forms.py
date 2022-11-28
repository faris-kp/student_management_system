from django import forms

from student_management_app.models import Courses,SessionYearModel

class DateInput(forms.DateInput):
    input_type = "date"

class AddStudentForm(forms.Form):
    email=forms.CharField(label="Email" ,max_length=50 ,widget=forms.EmailInput(attrs={"class":"form-control"}))
    password=forms.CharField(label="Password" ,max_length=50, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(label="First Name" ,max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name" ,max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="Username" ,max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    address=forms.CharField(label="Address" ,max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    courses=Courses.objects.all()
    course_list=[]
#     courses = {
#      'title' : 'awesome title',
#      'body' : 'great body of text',
#  }
    # session={
    #      'ti' : '333',
    #      'si' : '555',
    #  }

    for course in courses:
        small_course=(course.id, course.course_name)
        course_list.append(small_course)

    session_list=[]
    session = SessionYearModel.objects.all()
    for se in session:
        small_course=(se.id,str(se.session_start_year)+"  TO  "+str(se.session_end_year))
        session_list.append(small_course)
    gender_choices=(
        ("Male","Male"),
        ("Female","Female")
    )
    course=forms.ChoiceField(label="Course" ,choices=course_list, widget=forms.Select(attrs={"class":"form-control"}))
    sex=forms.ChoiceField(label="Gender" ,choices=gender_choices, widget=forms.Select(attrs={"class":"form-control"}))
    session_year_id=forms.ChoiceField(label="Session Year" ,choices=session_list, widget=forms.Select(attrs={"class":"form-control"}))
    profile_pic=forms.FileField(label="Profile Pic" ,max_length=50, widget=forms.FileInput(attrs={"class":"form-control"}))

class EditStudentForm(forms.Form):
    email=forms.CharField(label="Email" ,max_length=50 ,widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(label="First Name" ,max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name" ,max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="Username" ,max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    address=forms.CharField(label="Address" ,max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    courses=Courses.objects.all()
    print("course cheking ",courses)
#     courses = {
#      'title' : 'awesome title',
#      'body' : 'great body of text',
#  }

#     session={
#          'ti' : '333',
#          'si' : '555',
#      }
    course_list=[]
    for course in courses:
        small_course=(course.id, course.course_name)
        course_list.append(small_course)

    session_list=[]
    session = SessionYearModel.objects.all()
    for se in session:
        small_course=(se.id,str(se.session_start_year)+"  TO  "+str(se.session_end_year))
        session_list.append(small_course)
    
    gender_choices=(
        ("Male","Male"),
        ("Female","Female")
    )
    course=forms.ChoiceField(label="Course" ,choices=course_list, widget=forms.Select(attrs={"class":"form-control"}))
    sex=forms.ChoiceField(label="Gender" ,choices=gender_choices, widget=forms.Select(attrs={"class":"form-control"}))
    session_year_id=forms.ChoiceField(label="Session Year" ,choices=session_list, widget=forms.Select(attrs={"class":"form-control"}))
    profile_pic=forms.FileField(label="Profile Pic" ,max_length=50, widget=forms.FileInput(attrs={"class":"form-control"}),required=False)
