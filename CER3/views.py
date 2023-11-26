from django.shortcuts import render
from django.http import HttpResponse


<<<<<<< HEAD

# Create your views here.
=======
def index(request):
    title = "Inicio"
    data = {
        "title":title
    }  
    return render(request,'CER3/index.html',data)
>>>>>>> 9a288d5c6a7db7c4c1058b34f1161eefe2d03c0e
