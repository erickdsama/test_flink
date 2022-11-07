from rest_framework import serializers

from market_connection.exceptions import WrongCompanySymbol
from market_connection.modeling_prep_adapter import ModelingPrepAdapter
from market_connection.service import MarketConnectionService
from .models import Company

validate_service = MarketConnectionService(adapter=ModelingPrepAdapter())


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = "__all__"
        extra_kwargs = {"market_values": {"required": False, "allow_null": True}}

    def validate_symbol(self, value):
        try:
            validate_service.verify_symbol(value)
        except WrongCompanySymbol as e:
            raise serializers.ValidationError(e)
        return value

    def create(self, validated_data):
        validated_data['market_values'] = [
            value for value in validate_service.get_market_values(validated_data.get('symbol'))
        ]
        obj = super().create(validated_data)
        return obj
