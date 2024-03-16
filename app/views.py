from django.shortcuts import render
from .models import Publication 
# Create your views here.



def index(request):
    
    
    publications = Publication.objects.all()
    print(publications)
    
    context = {
        'publications': publications
    }
    
    return render(request, 'index.html', context=context)