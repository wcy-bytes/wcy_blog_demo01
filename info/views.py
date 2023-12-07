import os

from django.conf import settings
from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):

    home = Info.objects.filter(title='Home').first()

    # print(home)

    context = {
        'data': home
    }


    return render(request, 'info/infoMain.html', context)

def notes(request):

    notes = Info.objects.filter(title='Notes').first()

    print(notes)

    # print(home)

    context = {
        'data': notes
    }


    return render(request, 'info/infoMain.html', context)

def papers(request):

    papers = Info.objects.filter(title='Papers').first()

    # print(papers)

    context = {
        'data': papers
    }


    return render(request, 'info/infoMain.html', context)

def ynu(request):

    ynu = Info.objects.filter(title='YNU').first()

    context = {
        'data': ynu
    }


    return render(request, 'info/infoMain.html', context)

def lanping(request):

    lanping = Info.objects.filter(title='Lanping').first()

    context = {
        'data': lanping
    }


    return render(request, 'info/infoMain.html', context)

def closedFriends(request):

    closedFriends = Info.objects.filter(title='ClosedFriends').first()

    context = {
        'data': closedFriends
    }


    return render(request, 'info/infoMain.html', context)

def misc(request):

    misc = Info.objects.filter(title='Misc').first()

    context = {
        'data': misc
    }


    return render(request, 'info/infoMain.html', context)
