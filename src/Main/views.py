from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.request import Request

from rest_framework.response import Response
from rest_framework.views import APIView
import logging

class HealthCheckAPI(APIView):
    permission_classes=(AllowAny,)


    def get(self, request):
        data={
            'message': 'Incollege Auth Service Health OK',
            'method': str(self.request.method).lower()
        }
        return Response(data={'data': data}, status=status.HTTP_200_OK)


class DatabaseHealthCheckAPI(APIView):

    permission_classes=(AllowAny,)    

    def get(self, request):
        try :
            # login_session = login_sessions.objects.filter().first()  
            data={
                'message': 'MYE Auth Service Database Connection Health OK',
                'method': str(self.request.method).lower()
            }

          

            logging.info('Auth API SERVICE HEALTH IS OKAY')
            return Response(data={'data': data}, status=status.HTTP_200_OK)
      
        except : 
            return Response( status=status.HTTP_503_SERVICE_UNAVAILABLE)

        