
from re import template
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

<<<<<<< HEAD
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todolist.urls')), 
    path('register/', user_views.register, name = 'register'),
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name = 'login'), 
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name = 'logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name ='password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name ='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name ='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name ='password_reset_complete'),
    path('profile/', user_views.profile, name = 'profile'),
    path('profile/update/', user_views.update, name = 'profile-update'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
=======
urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + [
    path('admin/', admin.site.urls),
    path('', include('todolist.urls')), 
    path('register/', user_views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name = 'login'), 
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name = 'logout'),
    path('profile/', user_views.profile, name = 'profile'),
    path('update/', user_views.update, name = 'update'),
] 

>>>>>>> 5c6f3fc8b2eea0d7225e7b4b3f55d4cd27f8be7c
