from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from Upload.models import File
from .form import FileForm


class Home(TemplateView):
    template_name = 'home.html'


def file_list(request):
    files = File.objects.all()
    return render(request, 'file.html', {'files': files})


def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file')

    else:
        form = FileForm()
    return render(request, 'upload_file.html', {'form': form})
