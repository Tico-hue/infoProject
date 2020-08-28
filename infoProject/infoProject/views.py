from django.shortcuts import render
def Home(request):
    return render(request,'Home.html')

def Login(request):
    return render(request,'Login/login.html')