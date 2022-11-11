from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def code(request):
    return render(request, 'users/code.html')

def dashboard(request):
    return render(request, 'users/dashboard.html')