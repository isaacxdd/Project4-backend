from .models import Car
from rest_framework import serializers


## Class CarsSerializer is a subclass of serializers.HyperlinkedModelSerializer.
## For serializing and deserializing data into representations such as json.
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'brands', 'model', 'year', 'price', 'poster')