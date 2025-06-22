from django.urls import path
from .views import *

app_name = 'task_app'
urlpatterns = [

    # Tasks
    path('tasks', TaskListCreateView.as_view(), name="tasks"),
    path('tasks/<int:pk>', TaskDetailView.as_view(),name="tasks_detail"),
]