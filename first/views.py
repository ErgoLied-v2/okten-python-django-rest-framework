from rest_framework.response import Response
from rest_framework.views import APIView


class TestView(APIView):
    def get(self, *args, **kwargs):
        return Response('hello from get')

    def post(self, *args, **kwargs):
        return Response('hello from post')

    def put(self, *args, **kwargs):
        return Response('hello from put')

    def patch(self, *args, **kwargs):
        return Response('hello from patch')

    def delete(self, *args, **kwargs):
        return Response('hello from delete')
