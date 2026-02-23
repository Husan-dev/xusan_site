from django.shortcuts import render, redirect

from .forms import ContactForm
from .models import Project,CreateBlog,About,Contact,Experience,Skills,Service


def index(request):
    projects = Project.objects.all().order_by('-created_at')
    sites = CreateBlog.objects.all().order_by('-created_at')
    about = About.objects.all()
    experience = Experience.objects.all()
    skills = Skills.objects.all()
    service = Service.objects.all()

    forms = ContactForm(request.POST or None)
    if forms.is_valid():
        forms.save()
        return redirect('.')


    context = {
        'projects': projects,
        'sites': sites,
        'about': about,
        'experience': experience,
        'skills': skills,
        'forms': forms,
        'service': service,
    }
    return render(request, 'index.html', context)






