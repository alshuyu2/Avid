"""CapstoneProject595 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from fitness import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('home/', LoginView.as_view()),
    # path('login/', LoginView.as_view()),
    # path('createUser/', MyUserView.as_view()),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', views.homepage, name='homepage'),
    path('register', views.register_request, name='register'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('userpage/', views.userpage, name='userpage'),
    path('settings', views.settings, name='settings'),
    path('about', views.about, name='about'),
    path('edit_user', views.edit_user, name='edit_user'),
    path('upload/', views.image_upload_view, name='upload'),
    path('exercise_main', views.exercise_main, name='exercise_main'),
    path('exercise_add', views.exercise_add, name='exercise_add')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
