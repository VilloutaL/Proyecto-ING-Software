from django.shortcuts import render

# Create your views here.
def index(request):
    title = "Project of Ingeniería de software"
    return render(request, 'index.html', {"titulo" : title})