from django.shortcuts import render, redirect
from .forms import WaitListForm

# Create your views here.
def base(request):
    # Landing Page 
    if request.method == 'POST':
        form = WaitListForm(request.POST)
        if form.is_valid():
            form.save()
        
    else:
        form = WaitListForm()

    context = {
        'form': form
    }

    return render(request, 'base.html', context)