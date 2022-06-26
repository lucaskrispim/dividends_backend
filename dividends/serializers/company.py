# todo/todo_api/serializers.py
from rest_framework import serializers

from ..models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["name", "abbreviation", "sector"]

class CompanySerializerPandas(serializers.Serializer):
  id = serializers.IntegerField()
  name = serializers.CharField(max_length=30)
  abbreviation = serializers.CharField(max_length=30)
  sector = serializers.CharField(max_length=30)
  dy = serializers.FloatField()
  price = serializers.FloatField()

class CompanyAndDividensByPeriodSerializerPandas(serializers.Serializer):
  id = serializers.IntegerField()
  abbreviation = serializers.CharField(max_length=30)
  dy1 = serializers.FloatField()
  dy3 = serializers.FloatField()
  dy5 = serializers.FloatField()
  r1 = serializers.FloatField()
  r3 = serializers.FloatField()
  r5 = serializers.FloatField()