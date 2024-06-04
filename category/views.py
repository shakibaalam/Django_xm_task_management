from django.shortcuts import render,redirect
from . import forms
from . import models

def add_category(request):
    if request.method =='POST':
        category_form=forms.CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('add_category')
    else:
        category_form=forms.CategoryForm()
    return render(request, 'category/add_category.html',{'form':category_form})

def edit_category(request,id):
    post=models.CategoryModel.objects.get(pk=id)
    category_form=forms.CategoryForm(instance=post)
    if request.method =='POST':
        category_form=forms.CategoryForm(request.POST,instance=post)
        if category_form.is_valid():
            category_form.save()
            return redirect('home')
    return render(request, 'category/add_category.html',{'form':category_form})
    

def delete_category(request,id):
    post=models.CategoryModel.objects.get(pk=id)
    post.delete()
    return redirect('home')
