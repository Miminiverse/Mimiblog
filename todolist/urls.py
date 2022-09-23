
from django.contrib import admin
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
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
]