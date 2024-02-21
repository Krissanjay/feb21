from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    return render(request,"index.html")
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,"result.html",{'result':res})
# def register(request):
#     return render(request,"register.html")
# def login(request):
#     return render(request,"login.html")