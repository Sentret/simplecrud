from django.db import connection
from django.utils.deprecation import MiddlewareMixin
from django.template import Template, Context

class QueryCountDebugMidleware(MiddlewareMixin):
    def process_response(self, request, response):
        time = 0.0
        for q in connection.queries:
            time += float(q['time'])
        
        count = len(connection.queries)

        print ('Number of queries: %s\nExec time: %s' % (count ,time))         
        return response