from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse


def index(request):
    context = {}
    return render(request, 'trips/index.html', context)


def new(request):
    context = {}
    return render(request, 'trips/new.html', context)
