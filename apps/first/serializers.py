from rest_framework import serializers
from rest_framework.serializers import ValidationError

from apps.first.models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'price', 'year', 'body_type', 'created_at', 'updated_at',)

    def validate(self, data):
        if data['price'] == data['year']:
            raise ValidationError({'details': 'Price must be greater than or less to year'})
        return super().validate(data)

    def validate_year(self, year):
        if year == 2020:
            raise ValidationError({'details': 'Year must be not 2020'})
        return year
