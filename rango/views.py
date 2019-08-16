from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # Init context
    context_dict = {
        'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"
    }
    # Render page
    return render(request,
                  'rango/index.html',
                  context_dict)
                  
def about(request):
    # Init context
    context = {
        'my_name': 'Lloyd'
    }
    # Render page
    return render(request,
                  'rango/about.html',
                  context)