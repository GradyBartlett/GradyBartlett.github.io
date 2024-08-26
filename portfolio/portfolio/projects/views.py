from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    projects = Project.published.all()

    return render(request, 'portfolio/base.html', {'projects': projects})

def project_detail(request, id):
    project = get_object_or_404(Project, id=id, status=Project.Status.PUBLISHED)

    return render(request, 'portfolio/project/detail.html', {'project': project})

def experience(request):
    return render(request, 'portfolio/project/experience.html', {'projects': experience})

def about(request):
    return render(request, 'portfolio/project/about.html', {'projects': about})
