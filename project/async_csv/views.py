"""Declaring all views in async_csv app."""
from pathlib import Path
from rest_framework.views import APIView
from rest_framework.response import Response
from async_csv.tasks import sum_csv_file
from celery.result import AsyncResult
from celery import current_app


class FilesInteraction(APIView):
    """View to interact with csv files."""

    FILE_NOT_FOUND_RESPONSE = Response(
        {"errors": ["File not found"]},
        status=400)

    def get(self, request):
        """Get sum of csv file."""
        filename = request.GET.get('file')
        # checking if filename were mentioned in query params
        if filename is None:
            return self.FILE_NOT_FOUND_RESPONSE

        # generating filename
        filename = f'files/{filename}'
        file = Path(filename)

        # checking if file is exists
        if not file.is_file():
            return self.FILE_NOT_FOUND_RESPONSE
        print(filename)
        # creating task
        task = sum_csv_file.delay(filename)

        return Response({"task_id": task.id}, status=202)


class TaskManager(APIView):
    """Basic class for working with celery tasks."""

    def get(self, request, task_id):
        """Get info about task."""
        task_result = AsyncResult(task_id)
        result = {
            "task_id": task_id,
            "task_status": task_result.status,
            "task_result": task_result.result
        }
        return Response(result, status=200)


class ActiveTasks(APIView):
    """Getting all active celery tasks."""

    def get(self, request):
        """Get all active celery tasks."""
        # initializing gui for inspecting tasks
        inter = current_app.control.inspect()

        # tasks distro for each pc
        tasks = inter.active()
        return Response(tasks, status=200)
