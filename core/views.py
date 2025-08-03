from django.shortcuts import render
from .forms import SubmissionForm

def submit_view(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'submitted.html')
    else:
        form = SubmissionForm()
    return render(request, 'form.html', {'form': form})
