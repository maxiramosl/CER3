from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def index(request):
    title = "Inicio"
    data = {
        "title":title
    }  
    return render(request,'CER3/index.html',data)
