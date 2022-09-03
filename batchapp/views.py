from django.shortcuts import render, redirect

from batchapp.form import StudentForm
from batchapp.models import Student, Student1


def insert(request):
    if request.method =='GET':
        ob=StudentForm()
        return render(request,'insert.html',{'ob':ob})
    else:
        f=StudentForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('batchapp:insert')

def emp(request):
            ob = Student1.objects.all()
            return render(request, 'insert.html', {'ob': ob})

def insert(request):
            if request.method == 'GET':
                ob = StudentForm()
                return render(request, 'new.html', {'ob': ob})
            else:
                f = StudentForm(request.POST)
                if f.is_valid():
                    f.save()
                    return redirect('batchapp:emp')

def update(request, id):
            if request.method == "GET":
                ob = Student1.objects.get(id=id)
                return render(request, 'update.html', {'ob': ob})
            else:
                name = request.POST.get('name')
                age = request.POST.get('age')
                desi = request.POST.get('designation')
                sal = request.POST.get('salary')
                Student1.objects.filter(id=id).update(name=name, age=age, designation=desi, salary=sal)
            return redirect('batchapp:emp')