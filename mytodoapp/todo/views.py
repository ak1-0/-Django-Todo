from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Task
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

@csrf_exempt
def task_create(request):
    if request.method == 'POST':
        print("Received data:", request.POST)  # Для отладки
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return JsonResponse({
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'completed': task.completed
            }, status=201)
        print("Form errors:", form.errors)  # Для отладки
        return JsonResponse({'error': form.errors}, status=400)
    else:
        form = TaskForm()
    return render(request, 'todo/task_form.html', {'form': form})


@csrf_exempt
def task_update(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return JsonResponse({'id': task.id, 'title': task.title, 'description': task.description, 'completed': task.completed}, status=200)
    return JsonResponse({'error': 'Invalid data'}, status=400)

@csrf_exempt
def task_delete(request, pk):
    print(f"Request method: {request.method}")  # Выводим метод запроса
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully'}, status=204)
    return JsonResponse({'error': 'Method not allowed'}, status=405)