from django.shortcuts import render,redirect
from . import forms
from . import models

def add_task(request):
    if request.method =='POST':
        task_form=forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('add_task')
    else:
        task_form=forms.TaskForm()
    return render(request, 'task/add_task.html',{'form':task_form})

def edit_task(request,id):
    post=models.TaskModel.objects.get(pk=id)
    task_form=forms.TaskForm(instance=post)
    if request.method =='POST':
        task_form=forms.TaskForm(request.POST,instance=post)
        if task_form.is_valid():
            task_form.save()
            return redirect('home')
    return render(request, 'task/add_task.html',{'form':task_form})
    

def delete_task(request,id):
    post=models.TaskModel.objects.get(pk=id)
    post.delete()
    return redirect('home')
    
