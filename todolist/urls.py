
from django.contrib import admin
from django.urls import path
from . import views
<<<<<<< HEAD
#from .views import PostListView
#PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, create

urlpatterns = [

    #path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    #path('post/create/', PostCreateView.as_view(), name = 'post-create'), 
    #path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    #path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'), """
    
    path('admin/', admin.site.urls),
    path('home/',views.home, name='home'),
    path('post/<int:pk>/detail/', views.detail, name = 'post-detail'),
    path('post/create/', views.create, name='post-create'), 
    path('post/<int:pk>/delete/', views.delete_de, name = 'post-delete'),
    path('post/<int:pk>/update/', views.update, name = 'post-update'),
    path('task-list/', views.taskList, name = "task-list"),
    path('task-detail/<str:pk>', views.taskDetail, name = "task-detail"), 
    path('task-create/', views.taskCreate, name = "task-create"),
    path('task-delete/<str:pk>', views.taskDelete, name= "task-delete"),
=======
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',PostListView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/create/', PostCreateView.as_view(), name = 'post-create'), 
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
    path('add-list/', views.add, name='add-list'), 
    path('list/delete/<str:pk>', views.delete_de, name = 'delete_de'),
    path('list/update/<str:pk>', views.update, name = 'update'),
    path('task-list/', views.taskList, name = "task-list"),
    path('task-detail/<str:pk>', views.taskDetail, name = "task-detail"), 
    path('task-create/', views.taskCreate, name = "task-create"),
    path('task-delete/<str:pk>', views.taskDelete, name= "task-delete")
>>>>>>> 5c6f3fc8b2eea0d7225e7b4b3f55d4cd27f8be7c
]