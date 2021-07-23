from django.shortcuts import render
from .models import vote

def index(request):
    return render(request, 'vote/poll.html')

def add(request):
    votes = vote.objects.all()

    context = {'votes' : votes}
    return render(request, 'vote/vote.html', context)

def choose(request):
    return render(request, 'vote/choose.html')

def result(request):
    return render(request, 'vote/result.html')