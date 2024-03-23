from django.shortcuts import render
from.forms import imageForm
from.models import image

# Create your views here.
def home(request):
    if request.method == "post"
    form = imageForm(request.post,request.files)
    if form.is_valid():
      form.save()
    form = imageForm()
    img = image.objects.all()
    return render(request, 'myapp/home.html', {'form':form})
