from django.shortcuts import render,redirect
from .models import Student

# Create your views here
def index(request):
    stud = Student.objects.all()
    return render(request, "stud_dashboard/index.html", {'stud':stud})

def add_student(request):
    if request.method == 'POST':
        # print('added')
        # Retrieving all the inputs filled by the user
        regnum = request.POST.get('regnum')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        profile_pic = request.FILES.get('profile_pic')
        
        # Creating objects of the class "Student" using student as the obect
        student = Student()
        student.regnum=regnum
        student.fullname=fullname
        student.email=email
        student.address=address
        student.phone=phone
        student.profile_pic=profile_pic
        
        # saving all the inputs made by the student
        student.save() 
        return redirect('index')
    return render(request, 'stud_dashboard/add_student.html',{})
    
# function that handles the delete of each student by regnum 
def delete_student(request, regnum):
        student = Student.objects.get(pk=regnum)
        student.delete()
        return redirect('index')

# function that handles the update of each student by regnum 
def update_student(request, regnum):
        stud = Student.objects.get(pk=regnum)
        return render(request, 'stud_dashboard/update_student.html', {'stud': stud})

def edit_update_student(request, regnum):
    if request.method == 'POST':
        student = Student.objects.get(pk=regnum)
        student.regnum = request.POST.get('regnum')
        student.fullname = request.POST.get('fullname')
        student.email = request.POST.get('email')
        student.address = request.POST.get('address')
        student.phone = request.POST.get('phone')
        profile_pic = request.FILES.get('profile_pic')
        student.save()
    
        return redirect('index')
    
    return redirect('update_student', regnum=regnum)
         

    