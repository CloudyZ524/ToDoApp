from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task


# Create your views here.
def addTask(request):
    task = request.POST['task']    # get the text from POST
    Task.objects.create(task=task)   # create the object
    return redirect('home')        # redirect to homepage