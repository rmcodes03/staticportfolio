from django.shortcuts import render, get_object_or_404
from .models import Projects

# Create your views here.
def home(request):
    projects = Projects.objects
    return render(request, 'projects/home.html', {'projects': projects})

def projectdetails(request, project_id):
    projectdetail = get_object_or_404(Projects, pk=project_id)
    return render(request, 'projects/projectdetails.html', {'project' : projectdetail})