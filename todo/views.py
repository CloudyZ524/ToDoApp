from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task


# Create your views here.
def addTask(request):
    task = request.POST['task']    # get the text from POST
    Task.objects.create(task=task)   # create the object
    return redirect('home')        # redirect to homepage


def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)  # fetch the object with pk
    task.is_completed = True
    task.save()                 # save the change to task
    return redirect('home')


def mark_as_not_done(request, pk):
    task = get_object_or_404(Task, pk=pk)  # fetch the object with pk
    task.is_completed = False
    task.save()                 # save the change to task
    return redirect('home')


def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            "get_task" : get_task,
        }
        return render(request, 'edit_task.html', context)


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')