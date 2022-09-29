from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.

def index(request):

    todos = Todo.objects.all()
    todos = todos.order_by('priority')
    context = {
        'todos':todos
    }


    return render(request, 'todos/index.html',context)

def create(request):
    # 할 일 만든거
    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")
    Todo.objects.create(content=content,priority=priority,deadline=deadline)

    return redirect('todos:index')

def delete(request,todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()
    
    return redirect("todos:index")

def update(request,pk):

    todo = Todo.objects.get(pk=pk)
    print(todo)

    if todo.completed == 0:
        todo.completed = 1
        

    elif todo.completed == 1:
        todo.completed = 0
    todo.save()

    print(todo.completed)
    return redirect("todos:index")