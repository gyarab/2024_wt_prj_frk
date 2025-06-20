from django.shortcuts import render
from main.models import GPU

def get_homepage(request):
    context = {  
        # SELECT * from GPU ORDER BY 'title' LIMIT 20;
        "GPU": GPU.objects.all().order_by('title')
    }
    return render (request, "main/homepage.html", context)
