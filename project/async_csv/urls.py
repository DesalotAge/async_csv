"""Define urls patterns for async_csv app."""
from async_csv.views import (
    FilesInteraction,
    TaskManager,
    ActiveTasks
)
from django.urls import path

urlpatterns = [
    path('files/', FilesInteraction.as_view(), name="files_interaction"),
    path('tasks/<str:task_id>/', TaskManager.as_view(), name="task_manager"),
    path('tasks/', ActiveTasks.as_view(), name='active_tasks'),
]
