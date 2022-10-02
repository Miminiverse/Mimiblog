
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo
from .forms import TodoForm
<<<<<<< HEAD
#from django.views.generic import ListView 
#DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
=======
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

>>>>>>> 5c6f3fc8b2eea0d7225e7b4b3f55d4cd27f8be7c

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


<<<<<<< HEAD


"""
class PostDetailView(LoginRequiredMixin,DetailView):
    model = Todo

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Todo
    fields = ['title', 'text', 'date_posted']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

=======
def home(request):
    lists = Todo.objects.all()
    context = {'lists' : lists}
    return render(request, 'todolist/home.html', context)

class PostListView(ListView):
    model = Todo
    template_name = 'todolist/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    
class PostDetailView(DetailView):
    model = Todo
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Todo
    fields = ['title', 'text', 'date_posted']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
>>>>>>> 5c6f3fc8b2eea0d7225e7b4b3f55d4cd27f8be7c
    
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Todo
    fields = ['title', 'text', 'date_posted']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
<<<<<<< HEAD

=======
    
>>>>>>> 5c6f3fc8b2eea0d7225e7b4b3f55d4cd27f8be7c
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Todo
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
<<<<<<< HEAD
        return False """

def home(request):
    posts = Todo.objects.all()
    return render (request, 'todolist/todo_list.html', {'posts': posts})

def detail(request, pk):
    post = Todo.objects.get(id=pk)
    return render (request, 'todolist/todo_detail.html', {'post': post})

@login_required
def create(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():         
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')  
        return redirect('home')
    context = {'form' : form}
    return render (request, 'todolist/todo_form.html', context )

@login_required
def update(request, pk):
    post = Todo.objects.get(id=pk)
=======
        return False
    
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
>>>>>>> 5c6f3fc8b2eea0d7225e7b4b3f55d4cd27f8be7c
    form = TodoForm(instance=list)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
        return redirect ('home')
    
    context = {'form':form}
<<<<<<< HEAD
    return render (request, 'todolist/todo_form.html', context)

@login_required
=======
    return render (request, 'todolist/add_form.html', context)

>>>>>>> 5c6f3fc8b2eea0d7225e7b4b3f55d4cd27f8be7c
def delete_de(request, pk):

        Todo.objects.get(id=pk).delete()
        return redirect('home')
 
