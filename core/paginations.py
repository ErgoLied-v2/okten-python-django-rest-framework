from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PagePagination(PageNumberPagination):
    page_size = 5
    max_page_size = 10
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        count = self.page.paginator.count
        total_pages = self.page.paginator.num_pages

        return Response({
            'total_items': count,
            'total_pages': total_pages,
            'current_page': self.page.number,
            'data': data
        })

