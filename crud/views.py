from django.shortcuts import render,redirect
from .forms import Employee
from .models import User
# Create your views here.

def index(request):
    if request.method=='POST':
        fm=Employee(request.POST)
        if fm.is_valid():
            new=fm.save()
            new.save()
            return redirect('/')
    else:
        fm=Employee()
    data=User.objects.all()
    return render(request,'index.html',{'form':fm,'data':data})

def update(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=Employee(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        return redirect('/')
    else:    
        pi=User.objects.get(pk=id)
        fm=Employee(instance=pi)
    return render(request,'update.html',{'form':fm})

def delete_data(request,id):
    # if request.method=='POST':
    pi=User.objects.get(pk=id)
    pi.delete()
    return redirect('/')

