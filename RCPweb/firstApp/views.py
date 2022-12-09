from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from .forms import UploadForm

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def image_list(request):
    return render(request, 'list.html', {})

def upload_image(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = UploadForm()
    return render(request, 'upload.html', {
        'form': form
    })

