# views.py
from django.shortcuts import render, redirect
from .forms import MyModelForm

def upload_file_view(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_view')
        else:
            form = MyModelForm()
            return render(request, 'upload.html', {'form': form})