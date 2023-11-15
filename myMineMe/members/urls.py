
from django.urls import include,path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', include('members.urls')),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'), 
    path('admin/', admin.site.urls), 
]

