from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# from . import models
from list.models import task

# Create your views here.
def home(request):
    return render(request,"index.html")
def show(request):
    data = task.objects.all()
    return render(request,"show.html",{'data':data})
def send(request):
    if request.method == "POST":
        ID = request.POST['id']
        Task = request.POST['task']
        task(ID = ID , Task = Task).save()
        msg = "Task stored"
        return render(request,"index.html",{"msg":msg})
    else:
        return HttpResponse ("<h1>404 Not Found</h1>")
def delete(request):
    ID = request.GET['id']
    task.objects.filter(ID = ID).delete()
    return HttpResponseRedirect('show')
    
def edit(request):
    ID = request.GET['id']
    for data in task.objects.filter(ID = ID):
        Task = data.Task
    return render(request,"edit.html",{'ID':ID,'Task':Task})
def Recordedited(request):
    if request.method == 'POST':
        ID = request.POST['id']
        Task = request.POST['Task']
        task.objects.filter(ID = ID).update(Task=Task)
        return HttpResponseRedirect('show')
