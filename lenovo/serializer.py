from rest_framework import serializers
from .models import LenovoData


class LenovoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LenovoData
        fields = "__all__"






