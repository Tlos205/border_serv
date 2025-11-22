from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def activity(request):
    return render(request, 'activity.html')

def feedback(request):
    return render(request, 'feedback.html')

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

