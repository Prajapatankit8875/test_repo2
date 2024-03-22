from django.shortcuts import render
from.forms import imageForm
from.models import image

# Create your views here.
def home(request):
    form = imageForm()
    return render(request, 'myapp/home.html', {'form':form})
