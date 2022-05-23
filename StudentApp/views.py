from django.shortcuts import redirect, render
from .models import Student_details

# Create your views here.
def AddStudent(request):
    return render(request,'studReg.html')

def Stud_Reg(request):
    if request.method=='POST':
        name=request.POST['s_name']
        age=request.POST['s_age']
        address=request.POST['s_address']
        jdate=request.POST['s_joining_date']
        email=request.POST['s_email_id']
        qualif=request.POST['s_qualifications']
        gender=request.POST['s_gender']
        phn=request.POST['s_phone']
        
        students=Student_details(s_name=name,
                                 s_age=age,
                                 s_address=address,
                                 s_joining_date=jdate,
                                 s_email_id=email,
                                 s_qualifications=qualif,
                                 s_gender=gender,
                                 s_phone=phn
                                )
        students.save()
        print('Success')
        return redirect('show_stud')
    
    

def show_stud(request):
    students=Student_details.objects.all()
    return render(request,'show_student.html',{'students':students})

def editpage(request,pk):
    students=Student_details.objects.get(id=pk)
    return render(request,'edit_student.html',{'students':students})

def edit_student_details(request,pk):
    if request.method=='POST':
        students = Student_details.objects.get(id=pk)
        students.s_name = request.POST.get('s_name')
        students.s_email_id = request.POST.get('s_email_id')
        students.s_phone = request.POST.get('s_phone')
        students.save()
        return redirect('show_stud')
    return render(request, 'edit_student.html',)

def deletepage(request,pk):
    students=Student_details.objects.get(id=pk)
    return render(request,'dltStudent.html',{'students':students})

def delete_students(request,pk):
    students=Student_details.objects.get(id=pk)
    students.delete()
    return redirect('show_stud')

def student_details(request,pk):
    students=Student_details.objects.get(id=pk)
    return render(request,'student_details.html',{'students':students})



    
    

    