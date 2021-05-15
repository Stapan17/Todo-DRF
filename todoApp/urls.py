from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('todo-lists/', views.todoLists, name='todoLists'),
    path('todo-lists/<str:pk>/', views.todoDetails, name='todoDetails'),
    path('todo-create/', views.todoCreate, name='todoCreate'),
    path('todo-update/<str:pk>/', views.todoUpdate, name='todoUpdate'),
    path('todo-delete/<str:pk>/', views.todoDelete, name='todoDelete'),
]
