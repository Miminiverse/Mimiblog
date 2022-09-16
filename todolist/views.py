from pickle import FALSE
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo
from .forms import TodoForm

@api_view(['GET'])
def taskList(request):
    tasks = Todo.objects.all()
    serializer = TodoSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Todo.objects.get(id=pk)
    serializer = TodoSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Todo.objects.get(id=pk)
    task.delete()
    return Response(serializer.data)


def home(request):
    lists = Todo.objects.all()
    context = {'lists' : lists}
    return render(request, 'todolist/home.html', context)

def list(request, pk):
    list = Todo.objects.get(id=pk)
    context = {'list':list}
    return render(request, 'todolist/list.html', context)

def add(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

    context = {'form' : form}
    return render (request, 'todolist/add_form.html', context )

def update(request, pk):
    list = Todo.objects.get(id=pk)
    form = TodoForm(instance=list)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
        return redirect ('home')
    
    context = {'form':form}
    return render (request, 'todolist/add_form.html', context)

def delete_de(request, pk):

        Todo.objects.get(id=pk).delete()
        return redirect('home')
 
