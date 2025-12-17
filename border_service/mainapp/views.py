# mainapp/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from meta.views import Meta
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

    # ──────────────────────── SEO ДЛЯ СТРАНИЦЫ СПИСКА ВАКАНСИЙ ────────────────────────
    request.used_meta = Meta(
        title="Вакансии по контракту — Пограничное управление ФСБ России по Республике Карелия",
        description="Актуальные вакансии военной службы по контракту в Карелии. "
                    "Денежное довольствие от 80 000 ₽. Полный социальный пакет, жильё, льготы военнослужащим.",
        keywords=[
            "военная служба по контракту",
            "вакансии пограничной службы",
            "ФСБ Карелия",
            "контракт в пограничных войсках",
            "работа в ФСБ"
        ],
        image="meta/vacancies-list.jpg",           # положи картинку в media/meta/
        url=request.build_absolute_uri(),          # правильный canonical
        og_type="website",
        twitter_card="summary_large_image",
    )

    return render(request, 'contract_vacancies.html', {
        'vacancies': vacancies,
    })

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



def ultra_test(request):
    request.used_meta = Meta(
        title="Пограничное управление ФСБ России по Республике Карелия",
        description="Официальный сайт. Вакансии, новости, контакты.",
    )
    return render(request, 'test.html')