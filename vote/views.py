from django.shortcuts import render
from .models import vote, option


def index(request):
    return render(request, 'vote/poll.html')

def add(request):
    votes = vote.objects.all()

    context = {'votes' : votes}
    return render(request, 'vote/vote.html', context)

def choose(request, vote_id):
    options = option.objects.all()

    context = {'options' : options}
    return render(request, 'vote/choose.html', context)

def result(request, vote_id):
    return render(request, 'vote/result.html')