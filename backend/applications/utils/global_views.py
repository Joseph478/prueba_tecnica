
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from applications.utils.resp_tools import Resp
from applications.utils.custom_serializer import AppSerializerPaginate


class PaginatedListCreateView(ListCreateAPIView):
    pagination_class = AppSerializerPaginate
    serializer_response_page = None
    def list(self, request, *args, **kwargs):
        pagination = request.GET.get('page')
        if self.serializer_response_page is not None and pagination is not None:
            self.serializer_class = self.serializer_response_page
        
        return super().list(request)
    
    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            
            return Resp(data_=serializer.data, code_=status.HTTP_201_CREATED).send()
            
        return Resp(data_=serializer.errors, code_=status.HTTP_400_BAD_REQUEST, status_=False).send()
            

class AppRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated,)
    def retrieve(self, request, *args, pk):
        return Resp(msg_= str(self.queryset.model.__name__) +  " Encontrada", data_=self.get_serializer(self.get_object()).data).send()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Resp(data_=serializer.data, msg_= str(self.queryset.model.__name__) + " actualizado correctamente").send()
        
        return Resp(data_=serializer.errors, msg_="Error actualizar  " + str(self.queryset.model.__name__), status_=False, code_=status.HTTP_400_BAD_REQUEST).send()
        
    def destroy(self, request,*args, pk):
        instance = self.get_object()
        instance.state = False
        instance.save()
        return Resp(data_=self.get_serializer(instance).data, msg_= str(self.queryset.model.__name__) + " eliminado correctamente").send()