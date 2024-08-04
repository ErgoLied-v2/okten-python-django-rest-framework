from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from apps.cars.filter import CarFilter
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


class CarListView(ListAPIView):
    serializer_class = CarSerializer
    # queryset = CarModel.objects.less_than_year(2077).only_brand('vw')
    queryset = CarModel.objects.all()
    filterset_class = CarFilter


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
