from dataclasses import fields
from .models import IpList, AllowOrigin
from rest_framework import serializers


class IpListSerializer(serializers.ModelSerializer):
    class Meta:
        model = IpList
        fields = '__all__'


class AllowOriginSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllowOrigin
        fields = '__all__'
