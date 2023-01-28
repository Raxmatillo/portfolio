from django.shortcuts import render

from .models import Project



def index(request):
    projects = Project.objects.all()
    count = len(projects)
    context = {
        "projects":projects,
        "count":count
    }
    print(count)
    return render(request, "index.html", context)