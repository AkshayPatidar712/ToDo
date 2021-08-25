from django.shortcuts import redirect, render
from .forms import TaskForm
from .models import Task


def taskList(request):
    form = Task.objects.all()
    return render(request, 'list.html', {'form': form})


def taskAdd(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'index.html', {'form': form})
    else:
        form = TaskForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('list')


def taskUpdate(request, id):
    if request.method == 'GET':
        # update = Task.objects.get(pk=id)
        form = TaskForm(instance=(Task.objects.get(pk=id)))
        return render(request, 'index.html', {'form': form})
    else:
        # update = Task.objects.get(pk=id)
        form = TaskForm(request.POST, instance=(Task.objects.get(pk=id)))
    if form.is_valid():
        form.save()
        return redirect('list')


def taskDelete(request, id):
    form = Task.objects.get(pk=id)
    form.delete()
    return redirect('list')
