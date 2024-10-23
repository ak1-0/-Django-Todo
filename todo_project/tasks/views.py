from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.contrib.auth.decorators import login_required

@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'tasks/todo_list.html', {'todos': todos})

@login_required
def todo_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Todo.objects.create(title=title, description=description, user=request.user)
        return redirect('todo_list')
    return render(request, 'tasks/todo_form.html')

@login_required
def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.completed = 'completed' in request.POST
        todo.save()
        return redirect('todo_list')
    return render(request, 'tasks/todo_form.html', {'todo': todo})

@login_required
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'tasks/todo_confirm_delete.html', {'todo': todo})
