from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response

from core.permissions.is_admin_or_write_only import IsAdminOrWriteOnly

from apps.auto_parks.models import AutoParkModel
from apps.auto_parks.serializers import AutoParksSerializer
from apps.cars.serializers import CarSerializer


class AutoParkListCreateView(ListCreateAPIView):
    serializer_class = AutoParksSerializer
    queryset = AutoParkModel.objects.all()
    permission_classes = (IsAdminOrWriteOnly,)


class AutoParkAddCarView(GenericAPIView):
    queryset = AutoParkModel.objects.all()

    def post(self, *args, **kwargs):
        auto_park = self.get_object()
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_park=auto_park)
        parks_serializer = AutoParksSerializer(auto_park)

        return Response(parks_serializer.data, status.HTTP_201_CREATED)
