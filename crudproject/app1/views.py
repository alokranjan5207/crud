from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Employee
# Create your views here.
def index(request):
    return render(request=request,template_name='index.html')

def show(request):
    Employee.objects.all()
    return render(request=request,template_name='show.html')

def home(request):
    return render(request=request,template_name='home.html')

def send(request):
    if request.method=='POST':
        ID=request.POST['id']
        name=request.POST['name']
        course=request.POST['course']
        contact=request.POST['contact']
        Employee(ID=ID,name=name,course=course,contact=contact).save()
        msg='Data Stored Successfully'
        return render(request=request,template_name="home.html",context={'msg':msg})
    else:
        return HttpResponse("<h1>ERROR 404</h1>")

