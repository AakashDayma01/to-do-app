from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.add_task, name="home"),
    path("delete/<int:id>", views.delete_task, name="delete_task"),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
]
