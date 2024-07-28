from django.db.models import Q
from django.forms import model_to_dict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

from first.models import CarModel
from first.serializers import CarSerializer


class CarListCreateView(GenericAPIView):
    def get(self, *args, **kwargs):
        # queryset = CarModel.objects.filter(Q(brand__in=['audi', 'renault']) | Q(year=2077))
        # queryset = CarModel.objects.all()[2:4]   #pagination
        queryset = CarModel.objects.all()
        serializer = CarSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)

        # if not serializer.is_valid():
        #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class CarRetrieveUpdateDestroyView(GenericAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

    def get(self, *args, **kwargs):
        # pk = kwargs['pk']
        # try:
        #     car = CarModel.objects.get(pk=pk)
        # except CarModel.DoesNotExist:
        #     return Response('not found', status.HTTP_404_NOT_FOUND)

        car = self.get_object()
        serializer = CarSerializer(car)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        data = self.request.data
        # pk = kwargs['pk']
        # try:
        #     car = CarModel.objects.get(pk=pk)
        #
        # except CarModel.DoesNotExist:
        #     return Response('not found', status.HTTP_404_NOT_FOUND)

        car = self.get_object()
        serializer = CarSerializer(car, data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        data = self.request.data
        # pk = kwargs['pk']
        # try:
        #     car = CarModel.objects.get(pk=pk)
        # except CarModel.DoesNotExist:
        #     return Response('not found', status.HTTP_404_NOT_FOUND)

        car = self.get_object()
        serializer = CarSerializer(car, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        # pk = kwargs['pk']
        # try:
        #     car = CarModel.objects.get(pk=pk)
        #     car.delete()
        # except CarModel.DoesNotExist:
        #     return Response(status=status.HTTP_404_NOT_FOUND)

        self.get_object().delete()
        return Response('deleted', status.HTTP_204_NO_CONTENT)
