from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Project, Experience, Education, Contact
from .forms import ContactForm
import os
from datetime import datetime, timedelta
from git import Repo
from django.shortcuts import render
from git import Repo, InvalidGitRepositoryError, NoSuchPathError
from django.shortcuts import render, HttpResponse

def home(request):
    projects = Project.objects.all()[:3]
    experiences = Experience.objects.all().order_by('-start_date')
    return render(request, 'portfolio/home.html', {
        'projects': projects,
        'experiences': experiences,
    })

def about(request):
    profile = Profile.objects.first()
    education = Education.objects.all().order_by('-start_date')
    return render(request, 'portfolio/about.html', {
        'profile': profile,
        'education': education,
    })

def projects(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'portfolio/projects.html', {
        'projects': projects,
    })

def experience(request):
    experiences = Experience.objects.all().order_by('-start_date')
    return render(request, 'portfolio/experience.html', {
        'experiences': experiences,
    })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {
        'form': form,
    })
    
def git_contribution_dashboard(request):
    try:
        # Path to your local Git repository (adjust the path)
        repo_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".git")
        repo = Repo(repo_path)
        
        # Get the active branch (it will automatically detect the correct branch)
        branch = repo.active_branch if repo.head.is_valid() else None
        
        if not branch:
            return HttpResponse("No active branch found in the Git repository.", status=400)

        # Initialize contribution dictionary (last 365 days)
        contributions = {datetime.now().date() - timedelta(days=i): 0 for i in range(365)}
        
        # Fetch commit history
        for commit in repo.iter_commits(branch):
            commit_date = datetime.fromtimestamp(commit.committed_date).date()
            if commit_date in contributions:
                contributions[commit_date] += 1

        # Prepare data for the template
        context = {
            'contributions': contributions,
        }
        return render(request, 'git_dashboard.html', context)
    
    except (InvalidGitRepositoryError, NoSuchPathError):
        return HttpResponse("Invalid Git repository or path.", status=400)
