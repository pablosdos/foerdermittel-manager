
from django.db.models.base import Model
from rest_framework import serializers
from funding.models.funding import FundingSponsor
from funding.models import FundingProgramm
from rest_framework.serializers import ModelSerializer


class FundingSponsorSerializer(ModelSerializer):
    class Meta:
        model = FundingSponsor
        exclude = ['id']


class FundingProgramSerializer(ModelSerializer):

    region = serializers.CharField(source='get_region_display')
    type = serializers.CharField(source='get_type_display')
    area = serializers.StringRelatedField(many=True)

    sponsor = FundingSponsorSerializer(read_only=True)

    class Meta:
        model = FundingProgramm
        fields = '__all__'
