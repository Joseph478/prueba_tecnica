from rest_framework import status
from applications.utils.global_views import (
    AppRetrieveUpdateDestroyView,
    PaginatedListCreateView
)
from applications.tasks.models import Task
from applications.utils.resp_tools import Resp
from applications.tasks.serializers import (
    TaskSerializerRequest,
    TaskSerializerPaginate,
    TaskSerializerResponse
)


class TaskListCreateView(PaginatedListCreateView):
    queryset = Task.objects.active().order_by('-created_at')
    serializer_class = TaskSerializerRequest

class TaskDetailView(AppRetrieveUpdateDestroyView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializerResponse
