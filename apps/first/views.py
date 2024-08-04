from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.first.filter import car_filter
from apps.first.models import CarModel
from apps.first.serializers import CarSerializer


class CarListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return car_filter(self.request.query_params)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
