
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('list/<str:pk>', views.list, name='list'),
    path('add-list/', views.add, name='add-list'), 
    path('list/delete/<str:pk>', views.delete_de, name = 'delete_de'),
    path('list/update/<str:pk>', views.update, name = 'update'),
    path('task-list/', views.taskList, name = "task-list"),
    path('task-detail/<str:pk>', views.taskDetail, name = "task-detail"), 
    path('task-create/', views.taskCreate, name = "task-create"),
    path('task-delete/<str:pk>', views.taskDelete, name= "task-delete")
]