from rest_framework.views import APIView
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import permissions, status
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


# API для получения списка задач и создания новой задачи
class TodoListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        todos = Todo.objects.filter(user=request.user)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# API для работы с задачей по ID (получение, обновление и удаление)
class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]


@login_required
def todo_list_html(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'tasks/todo_list.html', {'todos': todos})


@login_required
def todo_create_html(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Todo.objects.create(title=title, description=description, user=request.user)
        return redirect('todo_list')
    return render(request, 'tasks/todo_form.html')


@login_required
def todo_edit_html(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()
        return redirect('todo_list')
    return render(request, 'tasks/todo_form.html', {'todo': todo})

@login_required
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.delete()
    return redirect('todo_list')