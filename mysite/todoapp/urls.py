from django.urls import path, include
from personal import views

urlpatterns = [
    path('', views.todoapp, name="todo_app"),
]
