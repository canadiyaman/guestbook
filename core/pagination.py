from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomEntryPagination(PageNumberPagination):
    page_size_query_param = "page_size"
    page_size = 3
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response(
            {
                "count": self.page.paginator.count,
                "page_size": self.page_size,
                "total_pages": self.page.paginator.num_pages,
                "current_page_number": self.page.number,
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
                "results": data,
            }
        )