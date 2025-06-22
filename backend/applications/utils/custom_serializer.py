from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class AppSerializerPaginate(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 25

    def get_paginated_response(self, data):
        return Response({
            'data': data,
            'previous': self.get_previous_link(),
            'next': self.get_next_link(),
            'message': "OK",
            'status': True,
            'count': self.page.paginator.count
        })
        