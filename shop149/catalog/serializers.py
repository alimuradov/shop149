from rest_framework import serializers
from .models import Pharmacy, Pill


class PharmacySerializer(serializers.ModelSerializer):

    class Meta:
        model = Pharmacy
        fields = '__all__'


class PillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pill
        fields = '__all__'