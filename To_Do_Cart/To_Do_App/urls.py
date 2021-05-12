from django.urls import path
from To_Do_App import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_todo/', views.add_todo),
    path('delete_todo/<int:todo_id>/', views.delete_todo),
    path('todo_completed/<int:todo_id>/', views.complete_todo),
    path('todo_incomplete/<int:todo_id>/', views.uncomplete_todo)
]
