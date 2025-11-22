# mainapp/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from .forms import FeedbackForm


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.send_email()
            messages.success(request, 
                "Ваше обращение успешно отправлено. "
                "В ближайшее время оно будет рассмотрено. Спасибо!")
            return redirect('feedback')
    else:
        form = FeedbackForm()
    
    return render(request, 'feedback.html', {'form': form})


def home(request):
    return render(request, 'index.html')

def activity(request):
    return render(request, 'activity.html')

def presscenter(request):
    return render(request, 'presscenter.html')

def contacts(request):
    return render(request, 'contacts.html')

def gosuslugi(request):
    return render(request, 'gosuslugi.html')

def leadership(request):
    return render(request, 'leadership.html')

def residents(request):
    return render(request, 'residents.html')

def service(request):
    return render(request, 'service.html')

def structure(request):
    return render(request, 'structure.html')



