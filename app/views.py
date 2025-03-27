from django.shortcuts import render
from .models import *

# Create your views here.
def index_view(request):
    info = Info.objects.last()
    context = {
        'info':info
    }
    return render(request, 'index.html', context)