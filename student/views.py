from django.shortcuts import render, redirect
from student.forms import StudentForm
from student.models import Student

# Create your views here.
def add(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view')
            except:
                pass
    else:
        form=StudentForm()
    return render(request,'add.html',{'form':form})

def view(request):
    students=Student.objects.all()
    return render(request,"view.html",{'students':students})

def delete(request,id):
    students=Student.objects.get(id=id)
    students.delete()
    return redirect('/view')

def edit(request,id):
    students=Student.objects.get(id=id)
    students = StudentForm(request.POST or None, instance=students)
    if students.is_valid():
        try:
            students.save()
            return redirect('/view')
        except:
            pass
    else:

        return render(request,"edit.html",{'students':students})
