from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination,
    CursorPagination
)    

class MyPageNumberPagination(PageNumberPagination):
    # Number of data should be on 1 page
    page_size = 5
    # We can access with p (?page=page no) instead of this we can simply use (?p=page no) in url
    page_query_param = 'p'
    # With the help of this someone can also control how much data should be in 1 page
    page_size_query_param = 'records'
    # The max value will be 7 if client want to control a pagination data
    max_page_size = 7
    # The last page name will be "end" instead of (?page=end)
    last_page_strings = 'end'

class MyLimitOffsetPagination(LimitOffsetPagination):
    # Number of data should be on 1 page
    default_limit = 5
    # We can access with mylimit (?mylimit=no of data & offset=no of data) instead of (?limit=no of data & offset=no of data)
    limit_query_param = 'mylimit'
    # We can access with myoffset (?limit=no of data & myoffset=no of data) instead of (?limit=no of data & offset=no of data)
    offset_query_param = 'myoffset'
    #  The max value of limit will be 7 even applying more than 7
    max_length = 7    

class MyCursorPagination(CursorPagination):
    # Number of data should be on 1 page
    page_size = 5
    # The name will be in ascending order
    ordering = 'name'   