# mainapp/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from .forms import FeedbackForm
from .models import News, Leader, Vacancy


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


def leadership(request):
    leaders = Leader.objects.all()
    chief = Leader.objects.filter(position='chief').first()
    deputies = Leader.objects.exclude(position='chief')
    return render(request, 'leadership.html', {
        'chief': chief,
        'deputies': deputies,
    })


def home(request):
    news = News.objects.filter(is_published=True).order_by('-pub_date')[:5]
    announcements = News.objects.filter(is_published=True, is_important=True).order_by('-pub_date')[:3]
    chief = Leader.objects.filter(position='chief').first()
    return render(request, 'index.html', {
        'news_list': news,
        'announcements': announcements,
        'chief': chief, # add for index page ТУТ повтор с функцией leadership
    })


def presscenter(request):
    all_news = News.objects.filter(is_published=True).order_by('-pub_date')
    return render(request, 'presscenter.html', {'all_news': all_news})

def contract_vacancies(request):
    vacancies = Vacancy.objects.filter(is_published=True).order_by('sort_order')
    return render(request, 'contract_vacancies.html', {'vacancies': vacancies})

def requirements(request):
    return render(request, 'requirements.html')

def activity(request):
    return render(request, 'activity.html')

def contacts(request):
    return render(request, 'contacts.html')

def gosuslugi(request):
    return render(request, 'gosuslugi.html')

def residents(request):
    return render(request, 'residents.html')


def service(request):
    return render(request, 'service.html')

def structure(request):
    return render(request, 'structure.html')
